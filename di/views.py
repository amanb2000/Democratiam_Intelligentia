from di import app
from flask import render_template

@app.route("/")
def instantiate_home():
    return render_template("schema1.html")
