import re
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from app.utils.insights_utils import generate_job_market_insights

insights_bp = Blueprint('insights', __name__)

@insights_bp.route('/market_insights', methods=['GET', 'POST'])
@login_required
def market_insights():
    insights = None
    if request.method == 'POST':
        role = request.form.get('role')  

        if not role:
            flash("Please select a job role!", "danger")
        else:
            try:
                raw_insights = generate_job_market_insights(role)

                if not raw_insights or raw_insights.strip() == "":
                    flash("AI did not return any insights. Please try again later.", "warning")
                else:
                    insights = re.sub(r'[#*]+', '', raw_insights)

            except Exception as e:
                print(f"[ERROR] LLM failed: {e}")
                flash("Something went wrong while contacting AI.", "danger")

    return render_template('market_insights.html', user=current_user, insights=insights)
