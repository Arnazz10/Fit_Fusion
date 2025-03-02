const sqlite3 = require('sqlite3').verbose();

// Connect to SQLite Database (or create if it doesn't exist)
const db = new sqlite3.Database(
  './users.db',
  sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE,
  (err) => {
    if (err) console.error(err.message);
    else console.log('Connected to SQLite database.');
  }
);

// Use serialize to run statements sequentially
db.serialize(() => {
  // Create Users Table
  db.run(`CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL
  )`);

  // Create Exercise Data Table
  db.run(`CREATE TABLE IF NOT EXISTS exercise_data (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user TEXT NOT NULL,
      squats INTEGER DEFAULT 0,
      toeTouches INTEGER DEFAULT 0,
      heelTouches INTEGER DEFAULT 0,
      hammerCurls INTEGER DEFAULT 0,
      lunges INTEGER DEFAULT 0,
      timestamp TEXT DEFAULT (datetime('now'))
  )`);

  // Insert sample data into the users table
  db.run(
    `INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?)`,
    ['Shubham Bhandari', 'shubham@example.com', 'password123']
  );
  db.run(
    `INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?)`,
    ['Ushnish', 'ushnish@example.com', 'password456']
  );
  db.run(
    `INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?)`,
    ['Arnab', 'arnab@example.com', 'password789']
  );

  // Insert sample data into the exercise_data table
  db.run(
    `INSERT OR IGNORE INTO exercise_data (user, squats, toeTouches, heelTouches, hammerCurls, lunges, timestamp)
     VALUES (?, ?, ?, ?, ?, ?, datetime('now','-1 day'))`,
    ['shubham@example.com', 20, 10, 5, 15, 8]
  );
  db.run(
    `INSERT OR IGNORE INTO exercise_data (user, squats, toeTouches, heelTouches, hammerCurls, lunges, timestamp)
     VALUES (?, ?, ?, ?, ?, ?, datetime('now','-2 days'))`,
    ['ushnish@example.com', 18, 12, 6, 10, 7]
  );
  db.run(
    `INSERT OR IGNORE INTO exercise_data (user, squats, toeTouches, heelTouches, hammerCurls, lunges, timestamp)
     VALUES (?, ?, ?, ?, ?, ?, datetime('now','-3 days'))`,
    ['arnab@example.com', 22, 8, 7, 12, 9]
  );
});

module.exports = db;
