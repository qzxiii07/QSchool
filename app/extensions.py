from flask_sqlalchemy import SQLAlchemy

# 初始化SQLAlchemy(extensions.py文件)
db = SQLAlchemy()   # 初始化SQLAlchemy

def init_extensions(app):  # 定义初始化函数
    db.init_app(app)    # 用app初始化SQLAlchemy