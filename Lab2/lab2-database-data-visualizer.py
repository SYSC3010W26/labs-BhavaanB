import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("sensorDB.db")

# Read table into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM sensordata", conn)

# Convert datetime string to datetime object
df["datetime"] = pd.to_datetime(df["datetime"])

# Plot data
plt.plot(df["datetime"], df["temperature"], label="Temperature")
plt.plot(df["datetime"], df["humidity"], label="Humidity")
plt.plot(df["datetime"], df["pressure"], label="Pressure")

plt.xlabel("Time")
plt.ylabel("Sensor Values")
plt.title("Sensor Data Over Time")
plt.legend()
plt.tight_layout()
plt.show()
