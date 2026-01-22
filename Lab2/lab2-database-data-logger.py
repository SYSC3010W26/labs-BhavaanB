import sqlite3
from datetime import datetime
from sense_hat import SenseHat
import time

sense = SenseHat()

conn = sqlite3.connect("sensorDB.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensordata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    temperature REAL,
    humidity REAL,
    pressure REAL
)
""")


while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    timestamp = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO sensordata (datetime, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
    """, (timestamp, temp, humidity, pressure))

    conn.commit()
    print("Logged data:", timestamp)
    time.sleep(1)

