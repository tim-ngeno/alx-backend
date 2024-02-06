#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    A config class to house the accepted language codes for the app
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
babel = Babel()

babel.default_locale = 'en'
babel.default_timezone = 'UTC'

# Use Config class as configuration for Flask app
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index template
    """
    return render_template(
        '0-index.html', title='Welcome to Holberton'
    )


if __name__ == "__main__":
    app.run(debug=False)
