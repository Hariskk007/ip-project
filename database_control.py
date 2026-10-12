import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "enter your password"
DB_NAME = "forge"


def init_db():

        db = mysql.connector.connect(host="localhost",user="root",password="Kumaresh%2585",database="test")
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS forge")
        db.commit()
        db.close()

        db = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email varchar(255) NOT NULL UNIQUE,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                role ENUM('admin', 'employee', 'user') DEFAULT 'user',
            )
        """)


        db.commit()
        db.close()

def get_user_by_username(username):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    db.close()
    return user

def check_username(username):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    ok=False
    if not user:
        ok=True
    db.close()
    return ok

def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    db.close()
    return user

def check_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    ok=False
    if not user:
        ok=True
    db.close()
    return ok

def create_user(email, username, password, role):
    """Inserts a new user into the database."""
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (email, username, password, role) VALUES (%s, %s, %s, %s)",
            (email, username, password, role))
        db.commit()
        success = True
    except mysql.connector.IntegrityError:
        success = False
    finally:
            db.close()
    return success

def find(username,password):
    db = get_db(username,password)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s and password = %s", (username,password))
    user = cursor.fetchone()
    ok=False
    if user:
        ok =True
    return ok

    
