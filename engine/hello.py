import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")

# def hello(name=2):

def hello(name=int(sys.argv[1])):
    return render_template('hello.html', name=name)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)