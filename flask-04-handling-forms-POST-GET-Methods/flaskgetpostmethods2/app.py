from flask import Flask, render_template, request




app = Flask(__name__)


def lcm(num1,num2):
    comman_multiplication = []
    for i in range(max(num1,num2), num1*num2+1):
        if i%num1==0 and i%num2==0:
            comman_multiplication.append(i)
    return min(comman_multiplication)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calc', methods=["POST","GET"])
def calculate():
    if request.method == "POST":
        num1 = request.form["number1"]
        num2 = request.form["number2"]
        return render_template("result.html", var1=num1, var2 = num2, result = lcm(int(num1),int(num2)),developer_name ="empo")
    else:
            return render_template("result.html",developer_name="empo")
            







if __name__ == "__main__":
    app.run(debug=True)
