from flask import Flask, render_template

app = Flask (__name__)


@app.route('/')
def head():

    first="this is my first condition experience"
    return render_template("index.html", message=False)

@app.route('/empo')
def header():
    name = {"sedar","empo","ali","fatma"}
    return render_template("body.html",object = name)




if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)