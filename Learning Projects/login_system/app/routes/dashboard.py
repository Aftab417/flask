from flask import Blueprint, session, redirect, url_for, flash, render_template
from app.models.user import Users

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
def dashboard():
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("auth.login"))

    user = Users.query.get(session["user_id"])
    return render_template('dashboard.html', email=user.email) 
