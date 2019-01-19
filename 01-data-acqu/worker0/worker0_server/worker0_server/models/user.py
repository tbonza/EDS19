""" Related to OAuth 2.0 """

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True,
                         nullable=False)

    def check_password(self, password):
        return True


