from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import db
import re

auth_bp = Blueprint('auth', __name__)

#---- Register Route ----
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number=request.form.get('phone_number')
        age=int(request.form.get('age'))
        password = request.form.get('password')      
        password_confirm = request.form.get('password_confirm')  

        if not name or not email or not password or not password_confirm or not age or not phone_number:
            flash('All fields are required.', 'danger')
            return redirect(url_for('auth.register'))

        if not re.fullmatch(r'\d{10}', phone_number):
            flash("Phone number must be exactly 10 digits.", "danger")
            return redirect(url_for("auth.register"))

        if password != password_confirm:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('auth.register'))
        
        if age < 18:
           flash('You must be 18 years or older to register.', 'danger')
           return redirect(url_for('auth.register'))


        existing_user = User.query.filter_by(email=email).first() 
        if existing_user:
            flash("User already exists. Please log in!", "warning")
            return redirect(url_for('auth.login'))

        new_user = User(name=name, email=email, phone_number=phone_number , age=int(age))
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


#---- Login Route ----
@auth_bp.route('/login', methods=['GET', 'POST'])  
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.dashboard'))
        else:
            flash("Invalid email or password.", "danger")

    return render_template('login.html')


#---- Logout Route ----
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))
