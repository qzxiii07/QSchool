from app.models import Student  

@app.route('/')
def index():
    student = Student.query.first()   # 查询
    # 增删改
    db.session.commit()   # 提交会话 
