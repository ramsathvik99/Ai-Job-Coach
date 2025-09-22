from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from markupsafe import Markup
import markdown

from app.models import db, Prompt
from app.utils.prompt_playground_utils import generate_prompt_response

prompt_bp = Blueprint('prompts', __name__)

@prompt_bp.route('/prompt_lab', methods=['GET', 'POST'])
@login_required
def prompt_lab():
    ai_response_html = None
    if request.method == 'POST':
        prompt_text = request.form.get('prompt_text')

        if not prompt_text:
            flash('Prompt text cannot be empty.', 'error')
        else:
            try:
                ai_response = generate_prompt_response(prompt_text)

                new_prompt = Prompt(
                    prompt_text=prompt_text,
                    response=ai_response,
                    user_id=current_user.id
                )
                db.session.add(new_prompt)
                db.session.commit()

                ai_response_html = Markup(markdown.markdown(ai_response))

                flash('Prompt added successfully!', 'success')
            except Exception as e:
                ai_response_html = Markup("<p style='color:red;'>Error: " + str(e) + "</p>")
                flash('Error generating response.', 'error')

    user_prompts = Prompt.query.filter_by(user_id=current_user.id).order_by(Prompt.created_at.desc()).all()

    return render_template(
        'prompt_lab.html',
        prompts=user_prompts,
        ai_response=ai_response_html,
        user=current_user
    )
