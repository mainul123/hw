from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/datapassingdemo")
def datapassingdemo():
    v = "a variable with somethin"
    l = ['a','b','c','d','e']
    d = {'first':'Jane', 'last':'Smith'}
    lucky_number = random.randrange(0,100)
    return render_template("data.html",
                           v = v,
                           list = l,
                           d = d,
                           lucky = lucky_number)

app.run(debug=True, host="0.0.0.0", port=5000)
