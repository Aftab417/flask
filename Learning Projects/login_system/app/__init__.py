from flask import Flask, redirect, url_for  
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


#  Create DB instance
db=SQLAlchemy()


def creat_app():

    # Loads Environment variables
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')


    #  initialize db
    db.init_app(app)


    # register routes_bp
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')


    # -------- Home route -------
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))
    
    

    #---  Create db tables
    with app.app_context():
        db.create_all()

    return app    


