from flask import Flask, g
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin@123'
app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)
#conn = mysql.connect()
#cursor = conn.cursor()

# Define a route that queries the database
@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    return str(results)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

# Create test data
def create_test_data():
    cursor = mysql.get_db().cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
    mysql.get_db().commit()

if __name__ == '__main__':
    #create_test_data()
    app.run(port=8090, debug=True)

    create_test_data()