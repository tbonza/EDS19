from flask import Blueprint

from .oauth_provider import default_provider

auth = Blueprint('auth', __name__)
oauth = default_provider(auth)

from . import views


