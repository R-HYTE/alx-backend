#!/usr/bin/env python3
"""
Basic Flask app with a single route.
"""

from flask import Flask, render_template
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


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        The rendered HTML template for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
