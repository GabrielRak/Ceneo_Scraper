from app import app
from flask import render_template

greeting = "Hello flask"

@app.route('/')
@app.route('/index')
def index():
    return render_template("subpages/index.html.jinja")