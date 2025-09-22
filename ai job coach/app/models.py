from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    resumes = db.relationship('Resume', backref='user', lazy=True)
    cover_letters = db.relationship('CoverLetter', backref='user', lazy=True)
    tracker_entries = db.relationship('JobApplication', backref='user', lazy=True)
    prompts = db.relationship('Prompt', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Resume(db.Model):
    __tablename__ = 'resumes'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    job_description = db.Column(db.Text)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class CoverLetter(db.Model):
    __tablename__ = 'cover_letters'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text)
    content = db.Column(db.Text)
    generated_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<CoverLetter {self.job_title} for User {self.user_id}>"

class InterviewAnswer(db.Model):
    __tablename__ = 'interview_sessions'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text)
    user_response = db.Column(db.Text)
    ai_feedback = db.Column(db.Text) 
    score = db.Column(db.Float)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class JobApplication(db.Model):
    __tablename__ = 'job_tracker'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.Date, nullable=True)       
    ai_analysis = db.Column(db.Text)            

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    @staticmethod
    def get_stats_for_user(user_id):
        applications_sent = JobApplication.query.filter_by(user_id=user_id).count()
        interviews_scheduled = JobApplication.query.filter_by(user_id=user_id, status='Interview').count()
        offers_received = JobApplication.query.filter_by(user_id=user_id, status='Offered').count()
        
        return {
            'applications_sent': applications_sent,
            'interviews_scheduled': interviews_scheduled,
            'offers_received': offers_received
        }

class Prompt(db.Model):
    __tablename__ = 'prompts'
    id = db.Column(db.Integer, primary_key=True)
    prompt_text = db.Column(db.Text)
    response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
