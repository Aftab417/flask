
# request is the object in flask, whenever a user send some data flask wrap it inside request object.

# Following are the attributes of request object
#   request.method
#   request.form
#   request.files
#   request.args
#   request.json
#   request.path
#   request.url
#   request.header
#   request.cookies  




from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello User"


@app.route("/demo", methods=["GET", "POST"])
def demo():
    return {
        "method": request.method,
        "path": request.path,
        "url": request.url
    }





