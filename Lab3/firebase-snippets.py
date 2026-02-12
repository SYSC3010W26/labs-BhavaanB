import pyrebase
import random
import time
from sense_hat import SenseHat
sense = SenseHat()


# Create new Firebase config and database object
config = {
  apiKey: "AIzaSyDfTovqLX-vuObnkrtPuNR_OLJGtqrjhh8",
  authDomain: "lab3-58bff.firebaseapp.com",
  databaseURL: "https://lab3-58bff-default-rtdb.firebaseio.com",
  storageBucket: "lab3-58bff.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
username="BhavaanBalasubramaniam"
dataset = "sensehat"

def writeData():
    global key
    key = 0

    sensorData = {
        "temperature": sense.get_temperature(),
        "humidity": sense.get_humidity(),
        "pressure": sense.get_pressure()
    }

    db.child(username).child(dataset).child(key).set(sensorData)
    key += 1



    # Will be written in this form:
    # {
    #   "sensor1" : {
    #     "0" : 0.6336863763908736,
    #     "1" : 0.33321038818190285,
    #     "2" : 0.6069185320998802,
    #     "3" : 0.470459178006184,
    #   }
    # }
    # Each 'child' is a JSON key:value pair
    db.child(username).child(dataset).child(key).set(sensorData)
    key = key + 1
    time.sleep(1)

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



