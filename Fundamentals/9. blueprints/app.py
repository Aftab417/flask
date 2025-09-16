
##################--------------  Blurprints in Flask  ------------------###################
#  Blueprints in Flask is a way to  'organize your application'  into smaller reuseable modules.


##################--------------  Create Blurprints    ------------------###################

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

#  'auth'  ->  Blutprint name (used internally  &  for  'url_for')
#  __name__  ->  tells flask where to find templates/static files for this blueprint. 




##################--------------  Define routes in Blurprints    ------------------###################

@auth_bp.route('/login')
def login():
    return 'Login Page'


@auth_bp.route('/logout')
def logout():
    return 'Logout Page'




##################--------------  Register Blurprints in app.py    ------------------###################

from flask import Flask


def create_app():
    app = Flask(__name__)

    # imports blueprints
    from app.routes.auth import auth_bp
    from app.routes.dashboard import bashboard_bp


    #  Register them
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(bashboard_bp, url_prefix='/dashboard')

