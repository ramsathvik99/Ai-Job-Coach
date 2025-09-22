from app.utils.ai_utils import generate_response

def analyze_job_description(job_description):
    prompt = (
        "Analyze the following job description and provide the following:\n"
        "1. Key Responsibilities (bullet points)\n"
        "2. Required Skills (bullet points)\n"
        "3. Important Keywords to include in a resume\n\n"
        f"Job Description:\n{job_description}"
    )

    return generate_response(prompt)
