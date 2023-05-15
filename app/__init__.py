from flask import Flask
from app.config import SQLALCHEMY_DATABASE_URI
from app.extensions import db, admin, init_db
from flask_admin.contrib.sqla import ModelView

def create_app():
    # 创建 Flask 应用
    app = Flask(__name__)
    # app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # 初始化 db
    db.init_app(app)

    # 初始化 admin
    init_db(app)

    # 注册蓝图
    # from app.api import api_blueprint
    from app.web.views import web_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(web_blueprint)
    
    return app

# from .extensions import app, db  # 导入并实例化app和db

# @app.cli.command()
# def init_db():
#     db.create_all()  # 现在可以使用db了

# if __name__ == '__main__':
#    app.run(debug=True)  # 可以运行app

# nav = [
#     {'name': 'Home', 'url': '/'},
#     {'name': 'About', 'url': '/about'}, 
#     {'name': 'Contact', 'url': '/contact'}
# ]  

# def register_blueprints(app): 
#     # 进行蓝本注册
#     app.register_blueprint(web_bp)

# def register_extensions(app):
    
#     admin.init_app(app)

# def create_flask_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
#     db.init_app(app)

#     return app

# def create_flask_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    
#     db = db_factory(app)

#     register_extensions(app)
#     register_blueprints(app) 
    
#     @app.route('/')
#     def index():
#         return 'Hello!'
    
#     return app

# if __name__ == '__main__':
#     app = create_flask_app()
#     app.run(debug=True)

# # if __name__ == '__main__':
# #     app = create_app()
# #     app.run()