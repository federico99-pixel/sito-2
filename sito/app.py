from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home-2.html")


@app.route("/friends-map")
def friends_map():
    return render_template("friend_around_word.html")


@app.route("/contact")
def contact():
    return render_template("reach-out.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )