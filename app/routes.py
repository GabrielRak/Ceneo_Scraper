from app import app

greeting = "Hello flask"

@app.route('/')
@app.route('/index')
def index():
    return greeting