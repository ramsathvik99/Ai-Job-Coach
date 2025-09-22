import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from instance.config import Config

db=SQLAlchemy()
migrate=Migrate()
login_manager = LoginManager() 


def create_app():
    app=Flask(__name__,instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    login_manager.init_app(app)  
    login_manager.login_view = 'auth.login' 
    from app.models import User  

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.resume import resume_bp
    from app.routes.cover_letter import cover_letter_bp
    from app.routes.interview import interview_bp
    from app.routes.tracker import tracker_bp
    from app.routes.prompts import prompt_bp
    from app.routes.insights import insights_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(cover_letter_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(tracker_bp)
    app.register_blueprint(prompt_bp)
    app.register_blueprint(insights_bp)

    return app