# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create a function named `index` which uses template file named `index.html` 
# send three numbers as template variable to the app.py and assign route of no path ('/') 
@app.route('/')
def index():
    return render_template("index.html")


# calculate sum of them using inline function in app.py, then sent the result to the 
# "number.html" file and assign route of path ('/total'). 
# When the user comes directly "/total" path, "Since this is GET 
# request, Total hasn't been calculated" string returns to them with "number.html" file
@app.route('/total', methods = ["GET","POST"])
def total():
    if request.method == "POST":
        variable1 = request.form.get("value1") # request.form['value1']
        variable2 = request.form.get("value2")
        variable3 = request.form.get("value3")
        return render_template("number.html", total = int(variable1)+int(variable2)+int(variable3))

    else:
        return render_template("number.html")


# Add a statement to run the Flask application which can be debugged.
if __name__=="__main__":
    app.run(debug=True)