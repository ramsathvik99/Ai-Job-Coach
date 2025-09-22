import re
from app.utils.ai_utils import generate_response

def generate_interview_questions(position):
    prompt = f"""
You are an expert interviewer.

Generate 10 realistic, commonly asked interview questions for the role of a {position}.

- The questions should be clear and relevant to the job.
- Mix technical and behavioral questions.
- Do not include numbering, bullets, hashtags, or formatting like **bold** or markdown.
- Only return the plain text questions, one per line.
"""
    return generate_response(prompt)



def evaluate_answer(question, answer):
    prompt = f"""
You are an AI interview evaluator.

Question: {question}
Candidate's Answer: {answer}

If the answer is mostly correct and relevant to the question, respond with only:
Correct

If the answer is wrong, irrelevant, or unclear, respond with only:
Wrong
"""
    return generate_response(prompt).strip()
