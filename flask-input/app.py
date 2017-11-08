from flask import Flask, render_template
from flask import request, redirect
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    l = ['one','two','three','four','five']
    return render_template("about.html",l = l)

@app.route("/input", methods=["POST","GET"])
def input_demo():
    if request.method=="GET":
        return render_template("input.html")

    # We only accept GET and POSt so it must be POST
    name = request.form['name']
    age = request.form['age']
    lucky = random.randrange(1,100)
    return render_template("input.html",name=name, age=age,lucky=lucky)
    
app.run(debug=True,host="0.0.0.0",port=5000)
