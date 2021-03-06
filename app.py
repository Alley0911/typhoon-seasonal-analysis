from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        sel_year = request.form.get('Year')
        sel_month = request.form.get('Month')
        return render_template("results.html") 
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
