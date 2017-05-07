"""generosalitton.com web page"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Required to use Flask sessions and the debug toolbar
app.secret_key = "9js*jl;kK#HoaesjflksjRGkjsadfdiauoiweoaskdn760kA!"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Homepage."""
         
    return render_template('index.html')

#route for sending me an email, learn flask mail


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
