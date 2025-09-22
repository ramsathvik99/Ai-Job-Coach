from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv() 
from app import create_app

app=create_app()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/resume_upload')
def resume_upload():
    return render_template('resume_upload.html')

@app.route('/cover_letter')
def cover_letter():
    return render_template('cover_letter.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

@app.route('/prompt_lab')
def prompt_lab():
    return render_template('prompt_lab.html')

@app.route('/market_insights')
def market_insights():
    return render_template('market_insights.html')

if __name__ == '__main__':
    app.run(debug=True)
