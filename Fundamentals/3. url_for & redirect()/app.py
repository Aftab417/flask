from flask import Flask, request, url_for, redirect, render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string('''
    <a href="{{ url_for('home') }}">Home</a>
    <a href="{{ url_for('profile', username='Aftab') }}">Profile</a>
'''
    )


@app.route("/profile/<username>")
def profile(username):
    return f"Profile for {username}"


@app.route("/go_profile/<username>")
def go_profile(username):
    return redirect(url_for("profile", username=username))

 