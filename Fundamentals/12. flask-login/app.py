
##############----------------   Flask Login  -----------------################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required


app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

##--------  LoginManager()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'route to redirect if not loged in'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)



#---------- user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




#----- login_user
@app.route('/login')
def login():
    user = User.query.filter(email='aftabkhan1567ss@gmail.com')
    if user:
        login_user(user)



#------ logout_user
@app.route('/logout')
@login_required
def logout():
    logout_user()




#----- current_user
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello {current_user.username}, Welcome to dashboard'

