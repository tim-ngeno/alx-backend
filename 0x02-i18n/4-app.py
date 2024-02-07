#!/usr/bin/env python3
"""Update locale from URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    A config class to house the accepted language codes for the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


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


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index template
    """
    title = _('home_title')
    header = _('home_header')
    return render_template('4-index.html', title=title, header=header)


if __name__ == "__main__":
    app.run(debug=False)
