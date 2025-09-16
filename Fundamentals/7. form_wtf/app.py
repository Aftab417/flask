from flask import Flask, render_template, redirect, url_for, session, flash
from form import LoginForm, RegisterForm

app = Flask(__name__)

app.secret_key = 'mysecret'


# ----------  Mock DB  -----------
users = {}


@app.route('/')
def home():
    return redirect(url_for('login'))



# ---------  Register Page  ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users:
            flash('Username already exists, Please chose another one', 'error')
            return redirect(url_for('register'))
        else:
            users[username] = password
            flash('Registration successfull, Please Login', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)     

     

# ---------  Login Page  -----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users and users[username] == password:
            flash('Login Successfule', 'success')
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials, Try again', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)    



# ---------  dashboard Page  ----------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    else:
        flash('You need to Login First', 'error')



# --------  Logout  -----------
@app.route('/logout')
def logout():
    flash('Successfully Loged out', 'info')
    session.pop('user')
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)