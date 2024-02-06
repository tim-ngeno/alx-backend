#!/usr/bin/env python3
""" Parameterize templates and Translations """

from flask import Flask, render_template, request
from flask_babel import Babel

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
        '3-index.html', title='Welcome to Holberton'
    )


if __name__ == "__main__":
    app.run(debug=False)
