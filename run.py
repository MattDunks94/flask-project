import os
from flask import Flask, render_template


app = Flask(__name__)

# Using @app.route("/"), this opens our index.html page.
# The route is a "/" because in our url there is nothing at the end of it.


@app.route("/")
def index():
    return render_template("index.html")

# This connects to our about.html page.
# The route is "/about" because in our url at the end of it is "/about."


@app.route("/about")
def about():
    return render_template("about.html")


# This connects to our contact.html page.
# The route is "/contact" because in our url at the end of it is "/contact."


@app.route("/contact")
def contact():
    return render_template("contact.html")


# This connects to our careers.html page.
# The route is "/careers" because in our url at the end of it is "/careers."


@app.route("/careers")
def careers():
    return render_template("/careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
