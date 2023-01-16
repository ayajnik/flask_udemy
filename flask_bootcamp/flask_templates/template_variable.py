#### we will be using Jinja template
#### as part of template variable you can pass list and dictionaries as well. When calling the render template module from the function, add a variable name after html file name
## and then assign the variable to that variable. 

##these variable can then be called into html file by using {{ }} syntax

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    some_variable = "Ayush"
    variable_list = list(some_variable)
    variable_dict = {"pup_name":"Sammy"} 
    return render_template("template_variable.html", my_variable = some_variable, my_list_variable=variable_list, my_dict_variable=variable_dict)

if __name__ == "__main__":
    app.run(debug=True)

