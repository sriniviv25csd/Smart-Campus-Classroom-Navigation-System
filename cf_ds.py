import sqlite3
conn = sqlite3.connect("classroom.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS classrooms (
    room_number TEXT PRIMARY KEY,
    building TEXT,
    floor TEXT,
    room_type TEXT
)
""")

classrooms = [
    ("008", "CC Block", "Ground Floor", "Lab"),
    ("001", "CC Block", "Ground Floor", "Lab"),
    ("015", "CC Block", "Ground Floor", "Lab"),
    ("012", "CC Block", "Ground Floor", "Lab"),
    ("013", "CC Block", "Ground Floor", "Lab"),
    ("096", "CC Block", "Ground Floor", "Classroom"),

    ("101", "A Block", "1", "Scholar"),
    ("102", "A Block", "1", "Drawing"),
    ("103", "A Block", "1", "Classroom"),
    ("106", "A Block", "1", "Classroom"),
    ("184", "A Block", "1", "Classroom"),

    ("127A", "A Block", "1", "Classroom"),
    ("219", "B Block", "2", "Classroom"),
    ("219A", "B Block", "2", "Classroom"),

    ("215", "B Block", "2", "Lab"),
    ("217", "B Block", "2", "Lab"),
    ("216", "B Block", "2", "Lab"),

    ("213", "B Block", "2", "Faculty"),
    ("201", "B Block", "2", "Classroom"),
    ("202", "B Block", "2", "Classroom"),
    ("204", "B Block", "2", "Classroom"),
    ("206", "B Block", "2", "Classroom"),
    ("206A", "B Block", "2", "Classroom"),

    ("205", "B Block", "2", "Office"),
    ("207", "B Block", "2", "Lab"),

    ("301", "C Block", "3", "Classroom"),
]

cursor.executemany("""
INSERT OR IGNORE INTO classrooms
(room_number, building, floor, room_type)
VALUES (?, ?, ?, ?)
""", classrooms)

conn.commit()
conn.close()

print("Classroom database created successfully!")
