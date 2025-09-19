from flask import Blueprint, session, redirect, url_for, flash, render_template
from flask_login import current_user, login_required 
from app.models.user import Users

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
@login_required
def dashboard():
    return render_template('dashboard.html', email=current_user.email) 
