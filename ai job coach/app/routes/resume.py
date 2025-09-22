import os
import markdown 
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models import db, Resume
from app.utils.resume_utils import get_resume_text, generate_resume_feedback, rewrite_section

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume_upload', methods=['GET', 'POST'])
@login_required
def resume_upload():
    if request.method == 'POST':
        ai_feedback = None
        resume_file = request.files.get('resumes')
        job_desc = request.form.get('job_description')
        
        if not resume_file or not job_desc:
            flash("Please upload a resume and enter the job description.", "danger")
            return redirect(url_for('resume.resume_upload'))

        try:
            resume_text = get_resume_text(resume_file)
        except Exception as e:
            flash(f"Error reading resume file: {e}", "danger")
            return redirect(url_for('resume.resume_upload'))

        feedback = generate_resume_feedback(resume_text, job_desc)

        new_resume = Resume(
            filename=resume_file.filename,
            job_description=job_desc,
            feedback=feedback,
            user_id=current_user.id
        )
        db.session.add(new_resume)
        db.session.commit()

        flash("Resume Uploaded and Analyzed successfully!", "success")

        html_feedback = markdown.markdown(feedback)

        return render_template('resume_upload.html', user=current_user, ai_feedback=html_feedback)

    return render_template('resume_upload.html', user=current_user)


@resume_bp.route('/rewrite_section', methods=['POST'])
@login_required
def rewrite_resume_section():
    section_text = request.form.get('section_text')
    if not section_text:
        return jsonify({"error": "No section text provided"}), 400

    rewritten_text = rewrite_section(section_text)
    return jsonify({"rewritten_text": rewritten_text})
