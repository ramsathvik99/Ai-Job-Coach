from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import JobApplication

dashboard_bp=Blueprint('dashboard',__name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    user_id = current_user.id
    stats =  JobApplication.get_stats_for_user(user_id)
    return render_template('dashboard.html',user=current_user,stats=stats)