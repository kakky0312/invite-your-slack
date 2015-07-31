from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField
from wtforms.validators import InputRequired, Length, Email
import requests
import json

app = Flask(__name__)

f = open('config.json', 'r')
data = json.load(f)


class EntryForm(Form):
    email = TextField('email', [InputRequired(), Email()])


@app.route('/slack-invite')
def index():
    form = EntryForm()
    return render_template('index.html', form=form, data=data, flag=False)


@app.route('/post', methods=['POST'])
def post():
    form = EntryForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        r = send_slack_invitation(email)
        if r['ok'] is True:
            return render_template('result.html', form=form)
        else:
            data['err_msg'] = 'Error: {}'.format(r['error'])
            return render_template(
                'index.html', form=form, data=data, flag=True
            )
    else:
        data['err_msg'] = 'Bad format: Please input E-mail address !!'
        return render_template('index.html', form=form, data=data, flag=True)


def send_slack_invitation(email):
    url = 'https://{}/api/users.admin.invite'.format(data['domain'])
    token = data['token']
    params = {'email': email, 'token': token, 'set_active': 'true'}
    return requests.post(url, params=params).json()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
