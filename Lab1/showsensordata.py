from sense_hat import SenseHat
import time


sense = SenseHat()

scroll_speed = 0.07

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

def get_sensor_data():
    temp = round(sense.get_temperature(), 1)
    pres = round(sense.get_pressure(), 1)
    hum = round(sense.get_humidity(), 1)
    
    
    message = f"Temp: {temp}C | Pressure: {pres}mb | Humidity: {hum}%"
    return message



try:
    while True:
    
        output_msg = get_sensor_data()
       
        sense.show_message(output_msg, scroll_speed, text_colour=white, back_colour=(0,0,0))
       
        time.sleep(1)

except KeyboardInterrupt:
 
    sense.clear()
    print("\nProgram stopped.")
