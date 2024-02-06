#!/usr/bin/env python3
""" Parameterize templates and translate languages """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel()


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
    Gets the language locale from request
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


# Use Config class as configuration for Flask app
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index template
    """
    return render_template(
        title=gettext('home_title'),
        header=gettext('home_header'),
        '3-index.html', title=title, header=header
    )


if __name__ == "__main__":
    app.run(debug=False)
