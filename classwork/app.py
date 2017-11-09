from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html",)

app.run(debug=True, host="0.0.0.0", port=5000)
