from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models import db, InterviewAnswer
from app.utils.interview_utils import generate_interview_questions, evaluate_answer

interview_bp = Blueprint('interviewanswers', __name__)

@interview_bp.route('/interviewanswers', methods=['GET'])
@login_required
def interview_page():
    return render_template('interview.html', user=current_user)

@interview_bp.route('/interviewanswers', methods=['POST'])
@login_required
def get_questions():
    role = request.form.get('role')
    if not role:
        return jsonify({'error': 'Role is required'}), 400

    questions_text = generate_interview_questions(role)
    questions = [q.strip() for q in questions_text.split('\n') if q.strip()]
    questions = questions[:10]

    return jsonify({'role': role, 'questions': questions})

@interview_bp.route('/save_interview_answer', methods=['POST'])
@login_required
def save_interview_answer():
    role = request.form.get('role')
    question = request.form.get('question')
    answer = request.form.get('answer')
    current_question_index = int(request.form.get('current_question_index', 0))

    if not role or not question or not answer:
        return jsonify({'error': 'All fields are required'}), 400

    new_answer = InterviewAnswer(
        role=role,
        user_response=question,
        answer=answer,
        user_id=current_user.id
    )
    db.session.add(new_answer)
    db.session.commit()

    return jsonify({'message': 'Answer saved successfully', 'next_index': current_question_index + 1})

@interview_bp.route('/evaluate_answer', methods=['POST'])
@login_required
def evaluate_answer_route():
    question = request.form.get('question')
    answer = request.form.get('answer')

    if not question or not answer:
        return jsonify({'error': 'Missing question or answer'}), 400

    feedback = evaluate_answer(question, answer)
    return jsonify({'feedback': feedback})
