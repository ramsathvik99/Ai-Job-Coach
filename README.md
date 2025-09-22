# AI Job Coach (Future Climb) - An AI based career based tool.

## Project Overview

In the Future Climb web application which is powered by LLM helps the user with:-
- Upload user resume and generate a feedback.
- Generate a cover letter based on the requirements.
- User can practise interview quetions based on the role user select.
- User can track the job they applied to.
- User can explore the job market with AI insights.
- User can enquire about anything using the prompts.

##  Features

- Resume Upload and AI-based Feedback
- Custom Cover Letter Generation using LLMs
- Interactive Interview Practice
- Job Application Tracker
- Prompt Playground and Job Market Insights

## Tech Stack

- Frontend: HTML, CSS, JS
- Backend:  FLASK(python)
- DATABASE: POSTGRESQL
- LLM API:  OPENROUTER

## Files Created

- app folder which contains all the main files like:
  *__init__.py
  *models.py
  - routes folder
  - static folder
  - templates folder
  - utils folder
- instance folder which contais the config.py file
- run.py file which contais the code to run the project.
- .env file which contains the database connection and secrete key and also the API key.
- future_climb.sql has the queries that are used to create the tables required for the project.

These are the files that are required to make the project running.

# Files Structure

|FUTURE CLIMB
│
├── app/
│   ├── STATIC/
│   │   ├── CSS/
│   │   ├── JS/
│   │   └── images/
│   ├── TEMPLATES/            
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── resume_upload.html
│   │   ├── cover_letter.html
│   │   ├── interview.html
│   │   ├── market_insights.html
│   │   ├── prompt_lab.html
│   │   ├── job_tracker.html
│   ├── models.py          
│   ├── ROUTES/             
│   │   ├── __init__.py        
│   │   ├── auth.py          
│   │   ├── insights.py          
│   │   ├── prompts.py          
│   │   ├── dashboard.py
│   │   ├── resume.py      
│   │   ├── cover_letter.py 
│   │   ├── interview.py      
│   │   └── tracker.py          
│   ├── UTILS/
│   │   ├── ai_utils.py              
│   │   ├── __init__.py             
│   │   ├── resume_utils.py           
│   │   ├── cover_letter_utils.py    
│   │   ├── interview_utils.py        
│   │   ├── job_tracker_utils.py     
│   │   ├── prompt_playground_utils.py 
│   │   └── insights_utils.py         
│   └── __init__.py                  
│
├── INSTANCE/
│   └── config.py             
├──.env            
├── future_climb.sql
├── requirements.txt           
├── run.py                   
└── README.md                


##  File and Folder Description
* run.py – Entry point to launch the Flask application.
* requirements.txt – Contains all Python dependencies required to run the project.
* .env – Stores sensitive environment variables like API keys, database URL, and secret key.
* future_climb.sql – SQL file for creating the PostgreSQL database schema.
* README.md – Project documentation file (you’re reading it).
* INSTANCE/config.py – Configuration file for different environments (development, production, etc.).

## STATIC – Static Assets
* CSS/ – Application UI custom stylesheets.
* JS/ – Frontend interactivity JavaScript files.
* images/ – Icons, logos, and other image resources.

## TEMPLATES – HTML Pages (Rendered by Flask)

* base.html – Shared layout used by all templates (navbar, footer).
* home.html – Public welcome page.
* login.html, register.html – Authentication pages.
* dashboard.html – User dashboard upon login.
* resume_upload.html – Resume upload and feedback page.
* cover_letter.html – Interface for AI-generated cover letter creation.
* interview.html – Practice job interviews with AI Q&A.
* market_insights.html – Displays LLM-driven job market trends and analytics.
* prompt_lab.html – Experimental playground to experiment with AI prompts.
* job_tracker.html – Track applications, interviews, and job statuses.

## ROUTES – Flask Route Blueprints (Modular Routing)
* __init__.py – Initializes and registers all Blueprints of routes.
* auth.py – Submits registration, login, and logout.
* dashboard.py – Manages routing and logic for user dashboard.
* resume.py – Manages text extraction from uploaded resumes, AI feedback on the same, and upload of resumes.
* cover_letter.py – Submits job descriptions to LLM and returns cover letters.
* interview.py – Manages interactive AI-driven interview simulation.
* tracker.py – Adds, updates, and deletes entries of job tracking.
* prompts.py – Handles custom prompt requests via prompt lab.
* insights.py – Displays LLM and other API-driven job market insights.

## UTILS – LLM and AI Integration Utility Functions
* __init__.py – Allows UTILS to be imported as a package.
* ai_utils.py – Consolidated functions for invoking the LLM API.
* resume_utils.py – Extracts and formats resume data, sends to LLM.
* cover_letter_utils.py – Generates cover letters from resumes and job descriptions.
* interview_utils.py – Produces job-oriented interview questions and feedback.
* job_tracker_utils.py – Utility functions to track user job applications.
* prompt_playground_utils.py – Handles dynamic prompt testing based on user input.
* insights_utils.py – Gathers and formats data for visualization of job market insight.

## models.py
* SQLAlchemy models for the entire app (users, resumes, feedback, etc.)
## __init__.py (root)
* Imports and initializes the Flask app, database, login manager, and loads config.


## How to Run the Future Climb Project

# 1. Download the Zip file 
Download the zip file and extract the folders from it and save them.

# 2. Set Up a Virtual Environment
python -m venv venv
venvScriptsactivate 

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Set Up Environment Variables
Create a .env file in the root directory and add the following:

DATABASE_URL=your_postgres_url
SECRET_KEY=your_secret_key
OPENROUTER_API_KEY=your_openrouter_api_key

# 5. Run the Application
run the flash application i.e run.py and
Open your browser and go to: http://127.0.0.1:5000/


####  Test Cases
Below are the key features of the AI Job Coach platform and the test cases used to verify their functionality.

### User Registration and Login

#### 1. Successful Registration
- Input: I submitted the registration form with:
  - Username: newuser
  - Email: newuser@example.com
  - Password: securepass123
- Expected Output: The user should be successfully registered and redirected to the login page or shown a success message.

#### 2. Duplicate Registration
- Input: I tried registering again with the same email or username.
- Expected Output: The system should show an error that the user already exists.

#### 3. Successful Login
- Input: I entered:
  - Username: newuser
  - Password: securepass123
- Expected Output: The system should log me in and redirect to the dashboard or homepage.

#### 4. Invalid Login
- Input: I entered a wrong password for an existing user.
- Expected Output: The system should show an "Invalid credentials" error message.



### Resume – Craft a Compelling Resume

#### 1. Upload Valid Resume
- Input: I uploaded a file named resume.pdf.
- Expected Output: The system should accept the file and extract resume details like name, skills, and experience.

#### 2. Upload Unsupported File
- Input: I tried to upload a .txt file.
- Expected Output: The system should reject the file and show an error message for unsupported format.

#### 3. Resume with No Content
- Input: I uploaded a blank PDF file.
- Expected Output: The system should show a message that the resume content could not be extracted.



### Cover Letter – Create a Tailored Cover Letter

#### 1. Generate Cover Letter with Valid Input
- Input: I filled the form with:
  - Job Title: Backend Developer
  - Job Description: Experience with Python and Flask
- Expected Output: A personalized cover letter should be generated and shown on the screen.

#### 2. Missing Job Description
- Input: I left the Job Description field empty.
- Expected Output: The system should show an error asking me to fill in the job description.



### Prompts – Get Inspired with Writing Prompts

#### 1. Use a Writing Prompt
- Input: I selected a prompt topic like "Tell me about yourself".
- Expected Output: The AI should return a suggested paragraph or idea based on the selected prompt.

#### 2. Submit Empty Prompt
- Input: I clicked Generate without typing anything.
- Expected Output: The system should show a validation error asking me to enter a prompt.



### Interview Practice – Practice Your Interview Skills

#### 1. Choose a Role and Get Questions
- Input: I selected Data Analyst as the role.
- Expected Output: A list of relevant interview questions should be displayed.

#### 2. Role Not Found
- Input: I typed a random/unsupported role name.
- Expected Output: The system should handle it gracefully and show a "No questions found" message or fallback options.



### AI Insights – Gain Insights from AI

#### 1. View Trending Job Skills
- Input: I selected the domain Data Science.
- Expected Output: The system should display a chart or list showing top skills and trends in that domain.

#### 2. External Data Fails
- Input: The system can't connect to external APIs.
- Expected Output: A friendly error should be displayed like "Unable to load insights, please try again later".



### Job Tracker – Manage Your Job Applications

#### 1. Add a New Job Application
- Input: I added details:
  - Company: Amazon
  - Role: Cloud Engineer
  - Status: Applied
- Expected Output: The entry should be saved and appear in the job tracker list with the provided details.

#### 2. Update Job Status
- Input: I changed the status from Applied to Interview Scheduled.
- Expected Output: The tracker should update the status correctly in the list.

#### 3. Delete Job Entry
- Input: I clicked delete for an existing job application.
- Expected Output: The job should be removed from the list.

#### 4. Submit Form with Missing Fields
- Input: I clicked submit without entering the company name.
- Expected Output: The system should show a message asking to fill all required fields.


### Future Enhacenments

- Email notifications for job tracker.
- Export resume feedback as PDF.
- Real-time chat with AI job coach.
- Get personolized quetions based on the resume.
- 
