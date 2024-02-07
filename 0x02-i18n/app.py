#!/usr/bin/env python3
"""Display the current time"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, gettext, _
import datetime
import pytz

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


# @babel.localeselector
def get_locale():
    """
    Gets the language locale from request or uses the default behaviour
    """
    # Check if `locale` is present in request args
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    # Check if user is logged in and has a preferred locale
    if g.user and g.user.get('locale') in Config.LANGUAGES:
        return g.user.get('locale')

    # Resort to default if locale arg is not present
    return request.accept_languages.best_match(Config.LANGUAGES)


# @babel.timezoneselector
def get_timezone():
    """
    Returns a valid timezone from URL params or from user settings if
    found, else defaults to 'UTC'
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate the provided timezone
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if user is logged in and has a preferred timzone setting
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to 'UTC' if no valid timezone is found
    return Config.BABEL_DEFAULT_TIMEZONE


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index template
    """
    title = _('home_title')
    header = _('home_header')
    welcome_message = _('logged_in_as', username=g.user['name']) \
        if g.user else _('not_logged_in')
    current_time = datetime.datetime.now(pytz.timezone(get_timezone()))
    formatted_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')
    current_time_msg = _('current_time_is %(current_time)s',
                         current_time=formatted_time)
    return render_template(
        'index.html', title=title, header=header,
        welcome_message=welcome_message,
        current_time_msg=current_time_msg
    )


if __name__ == "__main__":
    app.run(debug=False)
