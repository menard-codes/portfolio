from flask import Flask, json, jsonify, request
from flask_cors import CORS
import smtplib, ssl


app = Flask(__name__)
CORS(app)

@app.route('/email', methods=["POST"])
def get_req():
    print(dict(request.form))
    form = request.form
    context = ssl.create_default_context()
    sender_email = 'mmaranan.job@gmail.com'
    pass_ = 'git pull job'
    receiver_email = 'mmaranan.job@gmail.com'
    msg = f'''\
Subject: Job Prospect!

{form['name']} said:
{form['msg']}
contact:
    phone: {form['phone']}
    email: {form['email']}
'''
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password=pass_)
        server.sendmail(sender_email, receiver_email, msg)
    return ('', 204)

# if __name__ == '__main__':
#     app.run()
