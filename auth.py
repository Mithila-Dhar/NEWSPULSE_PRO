import bcrypt
from database import connect_db

def register_user(username, email, password, role="user"):
    conn = connect_db()
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users (username, email, password, role) VALUES (%s,%s,%s,%s)",
        (username, email, hashed, role)
    )

    conn.commit()
    conn.close()

def login_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    conn.close()

    if user and bcrypt.checkpw(password.encode(), user[3].encode()):
        return user
    return None
