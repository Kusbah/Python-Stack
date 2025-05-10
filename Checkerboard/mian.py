from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def checkeboard():
    return render_template("index.html",cols=8,rows=8)

@app.route('/<int:cols>')
def checkeboardx(cols):
    return render_template("index.html",cols=cols,rows=8)

@app.route('/<int:cols>/<int:rows>')
def checkeboardxy(cols,rows):
    return render_template("index.html",cols=cols,rows=rows)


if __name__ == "__main__":
    app.run(debug=True)