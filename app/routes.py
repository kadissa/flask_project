from flask import redirect, render_template, flash, url_for
from app import app
from app.forms import LoginForm


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'kadissa'}
    return render_template('index.html', user=user, title='home page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'пользователь {form.username.data} залогинился, '
              f'{form.remember_me.data=!s}')
        return redirect(url_for('index'))
    return render_template('login.html', title='login', form=form)


@app.route('/forum')
def forum():
    posts = [
        {
            'author': {'name': 'John'},
            'body': 'Welcome to New York'
        },
        {
            'author': {'name': 'Gogol'},
            'body': 'Не всякая птица долетит до середины днепра'
        }
    ]
    return render_template('forum.html', title='forum', posts=posts)
