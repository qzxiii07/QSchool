# from app import app   

# if __name__ == "__main__":
#     app.run() 

from app import create_app
from app.extensions import db, admin
    
app = create_app()
admin.init_app(app)

if __name__ == '__main__':
    app.run()