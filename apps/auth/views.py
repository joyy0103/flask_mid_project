from flask import Blueprint, redirect, render_template, request, url_for

from apps.auth.forms import LoginForm

# Blueprint를 사용해서 auth를 생성한다
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


# index 엔드포인트를 작성한다
@auth.route("/")
def index():
    return render_template("auth/login.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        return redirect(url_for("crud.friends"))
    return render_template("auth/login.html", form=form)
