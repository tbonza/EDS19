from flask import Blueprint

auth = Blueprint('auth', __name__)

from worker0_server.auth import views
