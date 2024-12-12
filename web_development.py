


# 1. Web Development (Python, SQL, Java, HTML)
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, term TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Search route
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM entries WHERE term LIKE ?", ('%' + search_term + '%',))
    results = c.fetchall()
    conn.close()
    return render_template('results.html', results=results)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)