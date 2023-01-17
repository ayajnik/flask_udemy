## we can use control flow statements in template variable like for loop and if statements.
## the syntax is as follows: {% %}

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    
    puppies = ["Rufus","Spotty","Bruno"]
    return render_template("template_control_flow.html", puppies=puppies)

if __name__ == "__main__":
    app.run(debug=True)