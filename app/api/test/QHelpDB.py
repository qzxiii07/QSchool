from flask import Flask, g
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin@123'
app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()

@app.before_first_request
def create_database():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    conn.commit()
    cursor.close()
    conn.close()

def create_table():
    None

@app.route("/")
def index():
    # 检测student_db数据库是否存在
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'student_db'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        # 不存在则创建数据库并添加5张表
        create_database() 
        create_table()
    # 继续显示首页内容
    return "Welcome!" 


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


class Student(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(50))
    gender = mysql.Column(mysql.String(10))
    birthday = mysql.Column(mysql.Date)
    enrollment_year = mysql.Column(mysql.Integer) 
    major_id = mysql.Column(mysql.Integer, mysql.ForeignKey('major.id'))

class Major(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(50))
    
class Course(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(50))
    credit = mysql.Column(mysql.Integer)
    major_id = mysql.Column(mysql.Integer, mysql.ForeignKey('major.id'))

class Selection(mysql.Model):
    student_id = mysql.Column(mysql.Integer,  mysql.ForeignKey('student.id'), primary_key=True)
    course_id = mysql.Column(mysql.Integer, mysql.ForeignKey('course.id'), primary_key=True) 
    grade = mysql.Column(mysql.String(10))
    year = mysql.Column(mysql.Integer)
    semester = mysql.Column(mysql.String(10))
    
class Teacher(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(20))
    gender = mysql.Column(mysql.String(10))  
    position = mysql.Column(mysql.String(20))
    major_id = mysql.Column(mysql.Integer, mysql.ForeignKey('major.id'))

@app.route("/")
def index():
    users = User.query.all()
    return str(users)