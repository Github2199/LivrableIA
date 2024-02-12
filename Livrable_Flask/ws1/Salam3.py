from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home1.html', message = "Hello World!")

@app.route("/next")
def suite():
    return render_template("page_suivante1.html")


if __name__ == "__main__":
    app.run()