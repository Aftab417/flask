# Import from flask 
from flask import Flask, request


# Create and object for Flask class
app = Flask(__name__)



# Creating routes
@app.route("/")
def home():
    return "Hello User!"


@app.route("/about")
def about():
    return "This is about page"


@app.route("/contacts")
def contacts():
    return "This is contact page"




# dynamic routes
@app.route("/profile/<username>")
def profile(username):
    return f"Profile for {username}"





#  Creating routes with methods
@app.route('/submit', methods=["GET", 'POST'])
def submit():
    if request.method == "POST":
        return "You sent something"
    else:
        return "You are just veiwing the Page"
    

    