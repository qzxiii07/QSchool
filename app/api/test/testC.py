from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL配置
conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="admin@123", 
    database="mydatabase"
)
cursor = conn.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

@app.route("/add", methods=["GET", "POST"]) 
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        return redirect("/")
    return render_template("add.html") 

if __name__ == "__main__":  
    app.run(debug=True)