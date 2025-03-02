from flask import Flask, request, jsonify, session
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a strong secret key
CORS(app, supports_credentials=True)

def get_db_connection():
    conn = sqlite3.connect("fitness_db.sqlite", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
cursor = conn.cursor()

# Create table for storing exercise counts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercise_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        squats INTEGER,
        toeTouches INTEGER,
        heelTouches INTEGER,
        hammerCurls INTEGER,
        lunges INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# Create table for users with username, email, and password
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
''')
conn.commit()

# ---------------------------
# User Registration & Login
# ---------------------------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        return jsonify({"error": "Missing username, email, or password"}), 400

    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, email, password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"})
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        session['email'] = email
        return jsonify({"message": "Login successful", "email": email})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# ---------------------------
# Exercise Data Endpoints
# ---------------------------
@app.route('/saveExercise', methods=['POST'])
def save_exercise():
    if 'email' not in session:
        return jsonify({"error": "User not logged in"}), 401

    email = session['email']
    data = request.json

    squats = data.get("squats", 0)
    toeTouches = data.get("toeTouches", 0)
    heelTouches = data.get("heelTouches", 0)
    hammerCurls = data.get("hammerCurls", 0)
    lunges = data.get("lunges", 0)

    try:
        cursor.execute('''
            INSERT INTO exercise_data (user, squats, toeTouches, heelTouches, hammerCurls, lunges)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (email, squats, toeTouches, heelTouches, hammerCurls, lunges))
        conn.commit()
        return jsonify({"message": "Exercise count saved!", "data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getExerciseData', methods=['GET'])
def get_exercise_data():
    if 'email' not in session:
        return jsonify({"error": "User not logged in"}), 401

    email = session['email']
    cursor.execute("SELECT * FROM exercise_data WHERE user = ?", (email,))
    result = cursor.fetchall()
    
    exercise_list = []
    for row in result:
        exercise_list.append({
            "id": row["id"],
            "user": row["user"],
            "squats": row["squats"],
            "toeTouches": row["toeTouches"],
            "heelTouches": row["heelTouches"],
            "hammerCurls": row["hammerCurls"],
            "lunges": row["lunges"],
            "timestamp": row["timestamp"]
        })
    
    return jsonify({"exercise_data": exercise_list})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
