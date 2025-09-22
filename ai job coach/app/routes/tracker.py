import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, JobApplication
from app.utils.job_tracker_utils import analyze_job_description
from datetime import datetime

tracker_bp = Blueprint('tracker', __name__)

@tracker_bp.route('/tracker', methods=['GET', 'POST'])
@login_required
def tracker():
    if request.method == 'POST':
        company = request.form.get('company')
        job_title = request.form.get('job_title')
        status = request.form.get('status')
        notes = request.form.get('notes')
        deadline_str = request.form.get('deadline')
        deadline = None

        if not company or not job_title or not status:
            flash("Please fill in all required fields!", "danger")
            return redirect(url_for('tracker.tracker'))

        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
            except ValueError:
                flash("Invalid deadline format. Use YYYY-MM-DD.", "danger")
                return redirect(url_for('tracker.tracker'))

        job_desc_to_analyze = notes if notes else job_title
        ai_analysis = analyze_job_description(job_desc_to_analyze)

        new_entry = JobApplication(
            company=company,
            job_title=job_title,
            status=status,
            notes=notes,
            deadline=deadline,
            ai_analysis=ai_analysis,
            user_id=current_user.id
        )
        db.session.add(new_entry)
        db.session.commit()
        flash("Job application added successfully!", "success")
        return redirect(url_for('tracker.tracker')) 

    return render_template('tracker.html', user=current_user)


@tracker_bp.route('/tracker/data')
@login_required
def tracker_data():
    applications = JobApplication.query.filter_by(user_id=current_user.id).all()
    return render_template('tracker_data.html', user=current_user, applications=applications)


@tracker_bp.route('/tracker/update/<int:application_id>', methods=['POST'])
@login_required
def update_application(application_id):
    application = JobApplication.query.get_or_404(application_id)

    if application.user_id != current_user.id:
        flash("Unauthorized access!", "danger")
        return redirect(url_for('tracker.tracker'))

    status = request.form.get('status')
    notes = request.form.get('notes')
    deadline_str = request.form.get('deadline')

    if status:
        application.status = status
    if notes:
        application.notes = notes

    if deadline_str:
        try:
            application.deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        except ValueError:
            flash("Invalid deadline format. Use YYYY-MM-DD.", "danger")
            return redirect(url_for('tracker.tracker'))
    else:
        application.deadline = None

    db.session.commit()
    flash("Application updated successfully!", "success")
    return redirect(url_for('tracker.tracker'))


@tracker_bp.route('/tracker/delete/<int:application_id>', methods=['POST'])
@login_required
def delete_application(application_id):
    application = JobApplication.query.get_or_404(application_id)

    if application.user_id != current_user.id:
        flash("Unauthorized access!", "danger")
        return redirect(url_for('tracker.tracker_data'))

    db.session.delete(application)
    db.session.commit()
    flash("Application deleted successfully!", "success")
    return redirect(url_for('tracker.tracker_data'))
