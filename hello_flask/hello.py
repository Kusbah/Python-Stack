from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello Flask"
@app.route('/test')
def test():
    return "this is a test route"


if __name__ == "__main__":
    app.run(debug=True)