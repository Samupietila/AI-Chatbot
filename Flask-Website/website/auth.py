from flask import Blueprint, render_template, request, flash, redirect, url_for
from Database import authentication
from flask_login import login_user, login_required, logout_user
from .models import User
from flask_babel import gettext as _
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        user = authentication.authenticate_user(username, password)
        if user:
            print(user)
            login_user(user, remember=True)
            flash(_('Logged in successfully!'), category='success')
            redirect(url_for('auth.thankyou'))
        else:
            flash(_('Username or password does not match'), category='error')
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/thankyou')
def thankyou():
    message = request.args.get('message', '')
    return render_template("thankyou.html", message = message)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if not email:
            print('Email is required')
            flash(_('Email is required'), category='error')
        elif password1 != password2:
            print('Passwords not matching')
            flash(_('Passwords are not matching'), category='error')
        elif len(password1) < 8:
            print("Password flash triggered")
            flash(_("Password must be greater than 7 characters"), category='error')
        elif len(username) < 4:
            print("Username flash has been triggered")
            flash(_("Lenght of Username must be more than 3"), category='error')
        else:
            emailCheck = authentication.emailCheck(email)
            usernameCheck = authentication.usernameCheck(username)
            if emailCheck:
                flash(_('Email address already exists'), category='error')
            elif usernameCheck:
                flash(_('Username is already in use'))
            if not emailCheck and not usernameCheck:
                authentication.register(email, username, password1)
                flash(_('Account has been created!'), category='success')
                language = request.cookies.get('language')
                message = authentication.get_localized_welcome_message(language)
                print(message)
                return redirect(url_for('auth.thankyou', message=message))
        
    return render_template("register.html")