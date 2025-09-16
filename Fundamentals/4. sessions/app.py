
#####################------------  sessions  ------------------########################
#   A session is a way to store data for a specific user across multiple request.
#   A session allows the server to remember the user while they browse your app.
#   A session is like a directory where your data is being stored in key, value pairs



from flask import Flask, request, url_for, redirect, session, render_template_string
app = Flask(__name__)
app.secret_key = 'superkey'

@app.route("/")
def home():
    return render_template_string('''
                                  
<form action="{{ url_for('login') }}" method="POST">
  <input type="text" name="username">
  <input type="password" name="password">                                  
  <button type="submit">Login</button>
</form>
''')

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    if "username" in session:
        return f"Welcom {session["username"]}"
    return "You are not loged in"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return "Loged out"
