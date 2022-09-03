import os
import json
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
    # This loads our company.json file as read-only ("r"), and assigns the data 
    # to the variable json_data.
    data = []
    with open("data/company.json", "r") as json_data:
        # We then assign our data variable to the json_data variable.
        data = json.load(json_data)
    # We then create new argument 'company' and assign it our variable data.
    return render_template("about.html", page_title="About", company=data)


# This connects to the members individual url's.
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# This connects to our contact.html page.
# The route is "/contact" because in our url at the end of it is "/contact."


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


# This connects to our careers.html page.
# The route is "/careers" because in our url at the end of it is "/careers."


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
