from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..repositories.user_repository import UserRepository
from ..repositories.order_repository import OrderRepository
from ..repositories.address_repository import AddressRepository

user_bp = Blueprint('user_routes', __name__, url_prefix='/user')

user_repo = UserRepository()
order_repo = OrderRepository()
address_repo = AddressRepository()

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
            flash("Registration successful! Please login.", "success")
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
            session['first_name'] = user.get('first_name', user['username'])
            return redirect(url_for('product_routes.list_products'))
        else:
            return render_template('user/login.html', error="Invalid email or password.")
            
    return render_template('user/login.html')


@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user_routes.login'))


@user_bp.route('/profile')
def view_profile():
    user_id = session.get('user_id') 
    if not user_id:
        return redirect(url_for('user_routes.login'))

    user = user_repo.get_by_id(user_id)
    addresses = address_repo.get_by_user_id(user_id)
    orders = order_repo.get_by_user_id(user_id)
    
    return render_template('user/profile.html', user=user, addresses=addresses, orders=orders)


@user_bp.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_routes.login'))
        
    if request.method == 'POST':
        update_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'phone_number': request.form.get('phone_number'),
        }
        
        if user_repo.update_user(user_id, update_data):
            flash("Profile updated successfully!", "success")
            return redirect(url_for('user_routes.view_profile'))
        else:
            flash("Error updating profile.", "error")
            
    user = user_repo.get_by_id(user_id)
    return render_template('user/edit_profile.html', user=user)