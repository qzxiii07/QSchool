from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
admin = Admin(template_mode='bootstrap3')

def create_db(app):
    with app.app_context():
        db.create_all()

def init_db(app):
    from app.models import Student,Major,Course,Selection,Teacher,User,Role

    admin.add_view(ModelView(Student, db.session)) 
    admin.add_view(ModelView(Major, db.session)) 
    admin.add_view(ModelView(Course, db.session)) 
    admin.add_view(ModelView(Selection, db.session))
    admin.add_view(ModelView(Teacher, db.session))
    admin.add_view(ModelView(User, db.session)) 
    admin.add_view(ModelView(Role, db.session)) 

    create_db(app)