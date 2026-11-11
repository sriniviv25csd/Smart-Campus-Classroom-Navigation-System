
from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

DB = os.path.join(os.path.dirname(__file__), "classroom.db")

@app.route("/")
def home():
    return "Smart Classroom Finder Backend Connected!"

@app.route("/classrooms")
def classrooms():
    try:
        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute("SELECT * FROM classrooms")
        data = cur.fetchall()
        con.close()
        return jsonify(data)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


