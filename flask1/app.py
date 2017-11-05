from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello</h1>"

@app.route("/about")
@app.route("/help")
def about():
    return "<h1>This is the about and help page</h1>"

@app.route("/longpage")
def longpage():
    s="""<h1>this is a title</h1>
    <hr/>
    <h2>with a subtitle</h2>
    <b>and some bold stuff</b>
    <hr/>
    <h1>and a bottom title</h1>
    """
    return s

app.run(debug=True,host="0.0.0.0",port=5000)
