from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #Database search here
        
        
        
        #Indend this correctly when function has been given
        return render_template("login.html")

@auth.route('/thankyou')
def logout():
    return render_template("thankyou.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if password1 != password2:
            print('Passwords not matching')
            flash('Passwords are not matching', category='error')
        elif len(password1) < 8:
            print("Password flash triggered")
            flash("Password must be greater than 7 characters", category='error')
        elif len(username) < 4:
            print("Username flash has been triggered")
            flash("Lenght of Username must be more than 3", category='error')
        else:
            flash('Account has been created!', category='success')
        
    return render_template("register.html")