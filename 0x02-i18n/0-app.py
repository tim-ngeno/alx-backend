#!/usr/bin/env python3
""" A basic flask app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns the index template
    """
    return render_template(
        '0-index.html', title='Welcome to Holberton'
    )


if __name__ == "__main__":
    app.run(debug=False)
