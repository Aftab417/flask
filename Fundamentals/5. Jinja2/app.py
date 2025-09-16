from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def profile():
    return render_template(
        "profile.html",
        title = "Student Profile",
        name = 'Aftab',
        is_toper = False,
        subjects = ["Math", "Science", "Computer"]
    )

    