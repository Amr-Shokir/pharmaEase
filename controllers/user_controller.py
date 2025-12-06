from flask import Blueprint, render_template, request, redirect, url_for, session
from repositories.user_repository import UserRepository

user_bp = Blueprint('user_routes', __name__, url_prefix='/user')
user_repo = UserRepository()

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not all([username, email, password]):
            return render_template('user/register.html', error="All fields are required.")

        try:
            user_repo.create_user(username, email, password)
            return redirect(url_for('user_routes.login'))
        except Exception as e:
            return render_template('user/register.html', error=f"Registration failed: {e}")

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = user_repo.authenticate(email, password)
        
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect(url_for('product_routes.list_products'))
        else:
            return render_template('user/login.html', error="Invalid email or password.")
            
    return render_template('user/login.html')


@user_bp.route('/profile')
def view_profile():
    user_id = session.get('user_id') 
    if not user_id:
        return redirect(url_for('user_routes.login'))

    user = user_repo.get_by_id(user_id)
    
    return render_template('user/profile.html', user=user)
