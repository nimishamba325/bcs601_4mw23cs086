from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        temp = float(request.form["temp"])
        conversion = request.form["conversion"]

        if conversion == "c_to_f":
            result = (temp * 9/5) + 32
            result = f"{temp}°C = {result:.2f}°F"
        else:
            result = (temp - 32) * 5/9
            result = f"{temp}°F = {result:.2f}°C"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
