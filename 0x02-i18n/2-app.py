#!/usr/bin/env python3
"""
Basic Flask app with BabelEx for internationalization.

This app serves a simple HTML page with "Welcome to Holberton" as the page
title and "Hello world" as the header. It supports internationalization with
English and French languages.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for setting Babel configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the user's preferred language.

    Returns:
        str: The best-matched language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
