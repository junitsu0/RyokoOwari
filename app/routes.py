from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, PostForm
from app.models import User, Post

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
        email = form.email.data
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('A user with that username or email already exists.', 'danger')
            return redirect(url_for('signup'))
            
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

# don't need posting
@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_post = Post(title=title, body=body, user_id=1)
        flash(f'{new_post.title} has been created.', 'secondary')
        return redirect(url_for('index'))

    return render_template('createpost.html', form=form)


# end dont need posting