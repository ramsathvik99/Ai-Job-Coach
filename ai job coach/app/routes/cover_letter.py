import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, CoverLetter
from app.utils.cover_letter_utils import generate_cover_letter
import markdown 
from markupsafe import Markup

cover_letter_bp = Blueprint('coverletter', __name__)

@cover_letter_bp.route('/coverletter', methods=['GET', 'POST'])
@login_required
def coverletter():
    if request.method == 'POST':
        job_title = request.form.get('job_title')
        job_desc = request.form.get('job_description')

        if not job_title or not job_desc:
            flash("Please Enter Job Title and Description!", "danger")
            return redirect(url_for('coverletter.coverletter'))

        ai_cover_letter = generate_cover_letter(job_title, job_desc)

        formatted_text = Markup(markdown.markdown(ai_cover_letter))

        new_cover_letter = CoverLetter(
            job_title=job_title,
            job_description=job_desc,
            generated_text=ai_cover_letter,
            user_id=int(current_user.id)
        )
        db.session.add(new_cover_letter)
        db.session.commit()

        flash("Cover letter submitted successfully!", "success")

        return render_template(
            'cover_letter.html',
            generated_text=formatted_text,  
            job_title=job_title,
            job_desc=job_desc,
            user=current_user
        )

    return render_template('cover_letter.html', user=current_user)
