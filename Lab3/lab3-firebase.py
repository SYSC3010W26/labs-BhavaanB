import pyrebase
import random
import time
from sense_hat import SenseHat
sense = SenseHat()

 
# Create new Firebase config and database object
config = {
  "apiKey": "AIzaSyDfTovqLX-vuObnkrtPuNR_OLJGtqrjhh8",
  "authDomain": "lab3-58bff.firebaseapp.com",
  "databaseURL": "https://lab3-58bff-default-rtdb.firebaseio.com",
  "storageBucket": "lab3-58bff.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
username="Bhavaan"
dataset = "sensehat"
key = 0
def writeData():
    global key

    sensorData = {
        "temperature": sense.get_temperature(),
        "humidity": sense.get_humidity(),
        "pressure": sense.get_pressure()
    }
    print("Writing to:", username, dataset, key)

    db.child(username).child(dataset).child(key).set(sensorData)
    key += 1

def readData():
    teammates = ["Ishaan", "Akshwin", "Aryan","Bhavaan"]  # add all team members

    for user in teammates:
        print(f"\n--- Last 3 values for {user} ---")

        data = db.child(user).child(dataset).get()

        # If no data yet
        if not data.each():
            print("No data yet.")
            continue

        entries = data.each()
        last_three = entries[-3:]  # last 3 entries

        for entry in last_three:
            print(entry.val())
while True:
    writeData()
    readData()
    time.sleep(2)



