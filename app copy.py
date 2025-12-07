from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    result = request.args.get("result", "0")
    num1 = request.args.get("")
    num2 = request.args.get("")
    return render_template("index.html", result=result, num1=num1, num2=num2)


@app.route("/add", methods=["POST"])
def add_two_numbers():
    if request.method == "POST":
        num1 = float(request.form.get("number1"))
        num2 = float(request.form.get("number2"))
        result = num1 + num2
        return redirect(url_for("index", result=result, num1=num1, num2=num2))


if __name__ == "__main__":
    app.run(debug=True)
