from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellow_puppy():
    return "<h1>Hello Puppy!!</h1>"

if __name__ == "__main__":
    app.run()