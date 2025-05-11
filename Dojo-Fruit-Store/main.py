from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count_strawberry = request.form['strawberry']
    count_raspberry = request.form['raspberry']
    count_apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count_all = int(count_apple)+int(count_strawberry)+int(count_raspberry)
    print(f"Charging {first_name} {last_name} for {count_all} fruits.")
    return render_template("checkout.html",strawberry=count_strawberry,raspberry=count_raspberry,apple=count_apple,first_name=first_name,
            last_name=last_name,id=student_id,all=count_all)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    