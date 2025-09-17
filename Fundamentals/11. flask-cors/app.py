from flask import Flask

from flask_cors import CORS

# Create app instance
app = Flask(__name__)


# Allow cors for all origin
CORS(app)



# Allow specific origin:
CORS(app, resources={r'/app/*', {'origin':'http://localhost:3000'}})


# Allow specific methods
CORS(app, methods=['GET', 'POST'])


# Allow headers
CORS(app, allow_headers=['Content-Type', 'Authorization'])