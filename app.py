from flask import Flask, render_template, flash, redirect, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'bjksdbfjksdbjgksbjgbdfgbjkdbfi'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'moizk3659@gmail.com'
app.config['MAIL_PASSWORD'] = 'nvru mxkw qtkm gjxr'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'moizk3659@gmail.com'

mail = Mail(app)

@app.route('/')
def contactPage():
    return render_template('contact.html')

@app.route('/send-mail', methods=['POST'])
def sendMail():
    name = request.form['name']
    subject = request.form['subject']
    message = request.form['message']
    
    if not name or not subject or not message:
        flash('All the fields should be provided')
        return redirect('/')

    msg = Message('YT Video Tutorial', recipients=[app.config['MAIL_USERNAME']])
    msg.body = f"Name= {name}\n subject= {subject}\n message= {message}"
    mail.send(msg)

    flash('email sent successfully')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)