#!/usr/bin/env python3
"""Implement a mock login system"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    A config class to house the accepted language codes for the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """
    Gets the language locale from request or uses the default behaviour
    """
    # Check if `locale` is present in request args
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    # Resort to default if locale arg is not present
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(user_id):
    """
    Returns a user dictionary or None if the ID is not found or login_as
    is not passed
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Uses `get_user` to find a user and set that user as global on flask.g.user
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id) if user_id else None


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index template
    """
    title = _('home_title')
    header = _('home_header')
    welcome_message = _('logged_in_as', username=g.user['name']) \
        if g.user else _('not_logged_in')
    return render_template(
        '5-index.html', title=title, header=header,
        welcome_message=welcome_message
    )


if __name__ == "__main__":
    app.run(debug=False)
