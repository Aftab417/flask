
#########################---------  url_for  ----------#############################
#   url_for is the function in flask that builds a URL dynamically for a given function name.
#   Instead of calling routes in hardcoded url path, we use "url_for("function name")"  




#  Usecase in Frontend:
#   we use url_for while calling any route


"""
<a href="{{ url_for('home') }}">Home</a>
<a href="{{ url_for('profile', username='Aftab') }}">Profile</a>

<form action="{{ url_for('login') }}" method="POST">
  <input type="text" name="username">
  <button type="submit">Login</button>
</form>

"""



# Usecase in backend:
#   in backend we use  url_for  to redirect to another url after onething is done



from flask import Flask, request, url_for, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcom Users"


@app.route("/login")
def login():
    # Afer login
    return redirect(url_for("home"))
 