from flask import Flask

app = Flask(__name__)


# Flask App Common Methods

app.run(host, port, debug)        # Start server
app.config[...]                   # App config settings
app.route("/path", methods=[])    # Define routes
app.add_url_rule()                # Add route manually

# Request Hooks
app.before_request(func)          # Runs before each request
app.after_request(func)           # Runs after each request
app.teardown_request(func)        # Runs after request (always)
app.before_first_request(func)    # Runs once before first request

# Error Handling
app.errorhandler(code)(func)      # Custom error pages

# Blueprints
app.register_blueprint(bp)        # Register blueprint

# Contexts
app.app_context()                 # Push app context
app.test_request_context()        # Fake request context

# Testing
app.test_client()                 # Test client for routes

# Logging
app.logger.info("msg")            # Log messages

# Static/Template helpers
app.send_static_file(filename)
app.open_resource(filename)
app.jinja_env                     # Template environment






#############-------------  Example code  --------------------#######################

from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"

@app.route("/")
def home():
    return "Hello Flask!"

@app.before_request
def before():
    app.logger.info("Before each request")

@app.after_request
def after(response):
    app.logger.info("After request")
    return response

@app.errorhandler(404)
def not_found(e):
    return "Oops! Page not found", 404

if __name__ == "__main__":
    app.run(debug=True, port=8080)
