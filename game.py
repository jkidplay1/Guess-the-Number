from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    session['number_to_guess'] = random.randint(1, 100)
    session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number_to_guess = session['number_to_guess']
    session['attempts'] += 1
    if guess < number_to_guess:
        message = 'Try higher!'
    elif guess > number_to_guess:
        message = 'Try lower!'
    else:
        message = f'Congratulations! You guessed it in {session["attempts"]} attempts!'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
