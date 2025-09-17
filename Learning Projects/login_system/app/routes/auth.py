from flask import Blueprint, render_template, redirect, url_for, session, flash
from app import db
from app.models.user import Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email
from werkzeug.security import generate_password_hash, check_password_hash


auth_bp = Blueprint('auth', __name__)


#--------  Registration Form  -----------
class Register_Form(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm_password', validators=[EqualTo('password', message='Password must be same')])
    submit = SubmitField('Register')



# ---------- Login Form  ------------
class Login_Form(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


 
#---------  Registeration route  ------------ 
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = Register_Form()
    if form.validate_on_submit():

        # Check for existing user
        existing_user = Users.query.filter(
            (Users.username == form.username.data) |
            (Users.email == form.email.data)
        ).first() 

        if existing_user:
            flash('User already exist', 'danger')
            return redirect(url_for('auth.register'))
        
        # Create new user
        hashed_password = generate_password_hash(form.password.data)
        new_user = Users(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Registration Successful')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

        


#----------  Login Route  ------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = Login_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first() 

        if user and check_password_hash(user.password, form.password.data ):
            session['user_id'] = user.id
            flash('Login successfull', 'success')
            return redirect(url_for('dashboard.dashboard')) 
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)    




#--------------  Logout  Route  ----------------
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None) 
    flash('You are logged out', 'info')
    return redirect(url_for('auth.login'))





