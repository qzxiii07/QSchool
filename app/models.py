from app.extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    birthday = db.Column(db.Date)
    enrollment_year = db.Column(db.Integer) 
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'))

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    credit = db.Column(db.Integer)
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'))

class Selection(db.Model):
    student_id = db.Column(db.Integer,  db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True) 
    grade = db.Column(db.String(10))
    year = db.Column(db.Integer)
    semester = db.Column(db.String(10))
    
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.String(10))  
    position = db.Column(db.String(20))
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))