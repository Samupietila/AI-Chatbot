from flask import Blueprint, render_template
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/thankyou')
def logout():
    return render_template("thankyou.html")

@auth.route('/register')
def sign_up():
    return render_template("register.html")