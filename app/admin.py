from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .extensions import db
from .models import User, Role   # 导入User和Role模型

# from app import create_flask_app

# app = create_flask_app()
# db = db_factory(app)

# # 创建管理员对象 
# admin = Admin(app)  

# # 添加模型管理视图
# admin.add_view(ModelView(User, db.session))  
# admin.add_view(ModelView(Role, db.session)) 

# # 定义初始化数据库的命令
# @app.cli.command()
# def init_db():
#     db.create_all()
#     print('数据库初始化完成!')


admin = Admin(name='Admin')

# 定义视图
admin.add_view(ModelView(User, db.session)) 