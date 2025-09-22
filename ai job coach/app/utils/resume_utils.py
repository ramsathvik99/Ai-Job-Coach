import PyPDF2
from app.utils.ai_utils import generate_response

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def get_resume_text(file):
    if file.filename.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file.filename.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        raise ValueError("Unsupported file format. Please upload .pdf or .txt files.")

def generate_resume_feedback(resume_text, job_desc=None):
    prompt = (
        "Please provide detailed feedback on this resume focusing on formatting, clarity, and key skills.\n"
        f"Job Description: {job_desc}\n" if job_desc else ""
    )
    prompt += "\nResume:\n" + resume_text
    return generate_response(prompt)

def rewrite_section(text):
    prompt = f"Rewrite this resume section to improve clarity and impact:\n{text}"
    return generate_response(prompt)
