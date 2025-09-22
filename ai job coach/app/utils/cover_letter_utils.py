from app.utils.ai_utils import generate_response

def generate_cover_letter(job_title, job_desc):
    prompt = (
        f"Write a professional cover letter tailored to this job title: {job_title}\n\n"
        f"Job Description:\n{job_desc}\n\n"
        f"The letter should be clear, persuasive, and highlight key skills relevant to the role."
    )
    return generate_response(prompt)

