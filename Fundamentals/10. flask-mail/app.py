from flask import Flask
from flask_mail import Mail, Message


# Create app instance
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your@gmail.com '
app.config['MAIL_PASSWORD'] = 'your password'


# create mail instance
mail = Mail(app)


# create msg instance
msg = Message(
    subject='checking in',
    sender='aftabkhan1567ss@gmail.com',
    recipients='aftabdevops0@gmail.com',
    body='How are you!'
)

#  HTML Emails
msg.html = '<b>Hello</b>, welcome to our service!'




# Attachments
with  app.open_resource('file.pdf') as fp:
    msg.attach('file.pdf', 'application/pdf', fp.read()) 





# Sends Email
mail.send(msg)