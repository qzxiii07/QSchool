from app import app, db, migrate
from flask_admin import Admin

@app.cli.command() 
def migrate():
    """数据库迁移命令"""
    migrate.init_app(app, db)
    migrate.migrate()
    migrate.upgrade()

@app.cli.command()
def create_admin():
    """创建管理员账号命令"""
    username = input('Enter admin username: ')
    password = input('Enter admin password: ')
    db.session.add(Admin(username=username, password=password))
    db.session.commit()
    print('Admin account created!')

@app.cli.command()
def runserver():
    """运行调试服务器命令"""
    app.run(debug=True)
    
# 其他自定义命令...

if __name__ == '__main__':
    app.run()