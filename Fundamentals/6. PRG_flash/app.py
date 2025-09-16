
from flask import Flask, render_template, redirect, url_for, flash, request, session

app = Flask(__name__)

app.secret_key = 'mysecret'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        if name == 'admin' and password == 'admin123':
            session['user'] = name
            flash('Login successfull', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials, Try again', 'error')
            return redirect(url_for('login'))
        
    return render_template('login.html')    



@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    else:
        flash('You must login first', 'error')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logout Successfully', 'info') 
    return redirect(url_for('login')) 



if __name__ == '__main__':
    app.run(debug=True)
