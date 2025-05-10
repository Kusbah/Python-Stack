from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/Champion')
def champion():
    return "Champion!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name+"!"

@app.route('/repeat/<int:num>/<name>')
def repeat(num,name):
    return (name + " ")*num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)