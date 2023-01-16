from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello puppy!!</h1>"

@app.route("/information")
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route("/puppy/<name>")
def puppy(name):
    return "<h1>This page is for {}</h1>".format(name)

if __name__ == "__main__":
    app.run()