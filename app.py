from flask import Flask, render_template, request, redirect, url_for
import email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email']
        message = request.form['message']

        if email.send_email('Nova mensagem de Entre em Contato', f'Nome: {name}\nEmail: {email_address}\n\nMensagem:\n{message}', 'seu_email@gmail.com'):
            return redirect(url_