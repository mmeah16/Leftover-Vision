from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import session

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = getUser(email)
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                print('Logging in .... redirecting to views.home')
                return redirect(url_for('views.home'))
            else:
                print('Incorrect password.')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(first_name) < 2:
            pass 
        elif password1 != password2:
            pass
        # elif len(password1) < 7:
        #     pass
        else:
            new_user = Users(email=email, name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            session.add(new_user)
            session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)


def getUsers():
    users = session.query(Users).all()
    return users

def getUser(email):
    user = session.query(Users).filter(Users.email == email).first()
    print(user.password)
    return user
