from app.utils.ai_utils import generate_response

def generate_job_market_insights(role):
    prompt = f"""
    You are a job market analyst. Provide insights about the role "{role}" including:
    1. Current market demand:
    2. Most required skills:
    3. Average salary in India and USA:
    4. Top companies hiring for this role:
    5. Tips for breaking into this field:
    """
    return generate_response(prompt)
