from flask import Flask
from robobrowser import RoboBrowser

app = Flask(__name__)

@app.route('/')
def hello():
    return ("go to /zodiacrecruitment/<postInformation> to send message\n\nArgs: email, password, messageLink separated by '&'")

@app.route('/zodiacrecruitment/<postInformation>')
def activateRecruitment(postInformation):
    print (postInformation)
    if (postInformation.count("&") == 2):
        email, password, messageLink = postInformation.split("&")

        # Logging in
        br = RoboBrowser(history=False, parser="lxml")
        br.open("https://politicsandwar.com/login")
        form = br.get_form(action='/login/')
        form["email"] = '{0}'.format(email)
        form["password"] = '{0}'.format(password)
        br.submit_form(form)

        messageLink = ("https://politicsandwar.com/inbox/message/receiver={0}".format(messageLink))
        # Sending message
        br.open(messageLink)
        form = br.get_form(action='')
        form["subject"] = 'hello'
        form["body"] = 'hello..'
        br.submit_form(form)

        return ("email ID: {0}\npassword: {1}\nmessageLink: {2}\n".format(email, password, messageLink))
    else:
        return ("information passed in wrong format")

app.run (debug = True)
