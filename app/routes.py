from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route('/')
def index():
    #this could be a database instead of dictionary
    user_info = {
        'username': 'justin',
        'email': 'jumanjiro@gmail.com'
    }
    games = ['Blackjack', 'Baccarat', 'Roulette', 'Craps', 'Three Card Poker', 'Four Card Poker', "Ultimate Texas Hold'em"]
    return render_template('index.html', user=user_info, games=games)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Form has been validated! Yippy Kai Yay')
        print(form.email.data, form.username.data, form.password.data)
    return render_template('signup.html', form=form)