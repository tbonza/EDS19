""" Views related to OAuth 2.0 """

from flask import g, render_template, request, jsonify
from sqlalchemy.orm import relationship
from flask_oauthlib.provider import OAuth2Provider
from flask_oauthlib.contrib.oauth2 import bind_sqlalchemy
from flask_oauthlib.contrib.oauth2 import bind_cache_grant

from . import auth
from ..models import User, Token, Client, Grant

def current_user():
    return g.user

def cache_provider(auth):
    oauth = OAuth2Provider(auth)

    bind_sqlalchemy(oauth, db.session, user=User,
                    token=Token, client=Client)

    app.config.update({'OAUTH2_CACHE_TYPE': 'simple'})
    bind_cache_grant(auth, oauth, current_user)
    return oauth

def sqlalchemy_provider(auth):
    oauth = OAuth2Provider(auth)

    bind_sqlalchemy(oauth, db.session, user=User, token=Token,
                    client=Client, grant=Grant, current_user=current_user)

    return oauth

def default_provider(auth):
    oauth = OAuth2Provider(auth)

    @oauth.clientgetter
    def get_client(client_id):
        return Client.query.filter_by(client_id=client_id).first()

    @oauth.grantgetter
    def get_grant(client_id, code):
        return Grant.query.filter_by(client_id=client_id, code=code).first()

    @oauth.tokengetter
    def get_token(access_token=None, refresh_token=None):
        if access_token:
            return Token.query.filter_by(access_token=access_token).first()
        if refresh_token:
            return Token.query.filter_by(refresh_token=refresh_token).first()
        return None

    @oauth.grantsetter
    def set_grant(client_id, code, request, *args, **kwargs):
        expires = datetime.utcnow() + timedelta(seconds=100)
        grant = Grant(
            client_id=client_id,
            code=code['code'],
            redirect_uri=request.redirect_uri,
            scope=' '.join(request.scopes),
            user_id=g.user.id,
            expires=expires,
        )
        db.session.add(grant)
        db.session.commit()

    @oauth.tokensetter
    def set_token(token, request, *args, **kwargs):
        # In real project, a token is unique bound to user and client.
        # Which means, you don't need to create a token every time.
        tok = Token(**token)
        tok.user_id = request.user.id
        tok.client_id = request.client.client_id
        db.session.add(tok)
        db.session.commit()

    @oauth.usergetter
    def get_user(username, password, *args, **kwargs):
        # This is optional, if you don't need password credential
        # there is no need to implement this method
        return User.query.filter_by(username=username).first()

    return oauth


def prepare_app(auth):
    db.init_app(auth)
    db.app = auth
    db.create_all()

    client1 = Client(
        name='dev', client_id='dev', client_secret='dev',
        _redirect_uris=(
            'http://localhost:8000/authorized '
            'http://localhost/authorized'
        ),
    )

    client2 = Client(
        name='confidential', client_id='confidential',
        client_secret='confidential', client_type='confidential',
        _redirect_uris=(
            'http://localhost:8000/authorized '
            'http://localhost/authorized'
        ),
    )

    user = User(username='admin')

    temp_grant = Grant(
        user_id=1, client_id='confidential',
        code='12345', scope='email',
        expires=datetime.utcnow() + timedelta(seconds=100)
    )

    access_token = Token(
        user_id=1, client_id='dev', access_token='expired', expires_in=0
    )

    access_token2 = Token(
        user_id=1, client_id='dev', access_token='never_expire'
    )

    try:
        db.session.add(client1)
        db.session.add(client2)
        db.session.add(user)
        db.session.add(temp_grant)
        db.session.add(access_token)
        db.session.add(access_token2)
        db.session.commit()
    except:
        db.session.rollback()
    return auth


def create_server(auth, oauth=None):
    if not oauth:
        oauth = default_provider(auth)

    auth = prepare_app(auth)

    @auth.before_request
    def load_current_user():
        user = User.query.get(1)
        g.user = user

    @auth.route('/home')
    def home():
        return render_template('auth/home.html')

    @auth.route('/oauth/authorize', methods=['GET', 'POST'])
    @oauth.authorize_handler
    def authorize(*args, **kwargs):
        # NOTICE: for real project, you need to require login
        if request.method == 'GET':
            # render a page for user to confirm the authorization
            return render_template('auth/confirm.html')

        if request.method == 'HEAD':
            # if HEAD is supported properly, request parameters like
            # client_id should be validated the same way as for 'GET'
            response = make_response('', 200)
            response.headers['X-Client-ID'] = kwargs.get('client_id')
            return response

        confirm = request.form.get('confirm', 'no')
        return confirm == 'yes'

    @auth.route('/oauth/token', methods=['POST', 'GET'])
    @oauth.token_handler
    def access_token():
        return {}

    @auth.route('/oauth/revoke', methods=['POST'])
    @oauth.revoke_handler
    def revoke_token():
        pass

    @auth.route('/api/email')
    @oauth.require_oauth('email')
    def email_api():
        oauth = request.oauth
        return jsonify(email='me@oauth.net', username=oauth.user.username)

    @auth.route('/api/client')
    @oauth.require_oauth()
    def client_api():
        oauth = request.oauth
        return jsonify(client=oauth.client.name)

    @auth.route('/api/address/<city>')
    @oauth.require_oauth('address')
    def address_api(city):
        oauth = request.oauth
        return jsonify(address=city, username=oauth.user.username)

    @auth.route('/api/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
    @oauth.require_oauth()
    def method_api():
        return jsonify(method=request.method)

    @oauth.invalid_response
    def require_oauth_invalid(req):
        return jsonify(message=req.error_message), 401

    return auth




