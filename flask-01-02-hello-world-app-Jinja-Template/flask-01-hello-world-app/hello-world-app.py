from flask import Flask
app = Flask(__name__)

@app.route('/')
def head():
    return "I like Flask"

@app.route('/second')
def swcond():
    return"this is the socond page"

@app.route('/third/subthird')
def third():
    return"this is the subpage of third page"


@app.route('/forth/<string:id>')
def forth(id):
    return f'id of this page is{id}'



if __name__=="__main__" :
    app.run(debug=True)

