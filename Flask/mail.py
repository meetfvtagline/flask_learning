from flask import Flask,request,render_template
from flask_mail import Message,Mail
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('MAIL_USERNAME')
PASS = os.getenv('MAIL_PASSWORD')

app=Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = USER
app.config['MAIL_PASSWORD'] = PASS
app.config['MAIL_PORT'] = 587

app.config['MAIL_DEFAULT_SENDER'] = USER

mail = Mail(app)


@app.route("/")
def index():
    return render_template('mail.html')

@app.route('/send', methods=['POST'])
def send_mail():
    recipient = request.form['email']
    message_body = request.form['message']

    msg = Message(
        subject="Message from Flask App",
        recipients=[recipient],
        body=message_body
    )

    mail.send(msg)
    return "Email sent successfully!"


if __name__ == '__main__':
   app.run(debug = True)

   