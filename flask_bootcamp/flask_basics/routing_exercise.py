from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Welcome! Go to /puppy_latin page to see your dog's puppy latin name</h1>"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):

    if str(name).endswith("us"):
        name = str(name).replace("us","y")
        return "<h1>Your puppy latin name is: {}</h1>".format(name)
    else:
        if str(name).endswith("y"):
            name = str(name).replace("y","iful")
            return "<h1>Your puppy latin name is: {}</h1>".format(name)

if __name__ == "__main__":

    app.run(debug=True)

