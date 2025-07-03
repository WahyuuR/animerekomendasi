import mysql.connector
from passlib.hash import bcrypt
from Modules.db_config import DB_CONFIG

def create_user_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username VARCHAR(50) PRIMARY KEY, password VARCHAR(255))''')
    conn.commit()
    conn.close()

def create_bookmark_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookmarks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50),
                    title VARCHAR(255),
                    FOREIGN KEY (username) REFERENCES users(username)
                 )''')
    conn.commit()
    conn.close()

def register_user(username, password, role="user"):
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    hashed = bcrypt.hash(password)
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, hashed, role))
        conn.commit()
        result = True
    except mysql.connector.IntegrityError:
        result = False
    conn.close()
    return result


def login_user(username, password):
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    c.execute("SELECT password, role FROM users WHERE username = %s", (username,))
    data = c.fetchone()
    conn.close()
    if data:
        stored_password = data[0]
        role = data[1]
        if bcrypt.verify(password, stored_password):
            return True, role
    return False, None

