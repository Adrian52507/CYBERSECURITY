from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Crear la base de datos y tabla si no existen
def create_db():
    conn = sqlite3.connect("visits.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS visit_counter (id INTEGER PRIMARY KEY, count INTEGER)''')
    cursor.execute("INSERT OR IGNORE INTO visit_counter (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

# Incrementar el contador de visitas
@app.route('/')
def index():
    conn = sqlite3.connect("visits.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE visit_counter SET count = count + 1 WHERE id = 1")
    conn.commit()
    cursor.execute("SELECT count FROM visit_counter WHERE id = 1")
    visit_count = cursor.fetchone()[0]
    conn.close()
    return render_template("index.html", visit_count=visit_count)

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
