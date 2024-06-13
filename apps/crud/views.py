from flask import Blueprint, render_template, redirect, url_for

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
def index():
    return redirect(url_for("auth.login"))

@crud.route("/friends")
def friends():
    return render_template("crud/friends.html")

@crud.route("/chats")
def chats_index():
    return render_template("crud/chats_index.html")

@crud.route("/chat")
def chat_index():
    return render_template("crud/chat_index.html")

