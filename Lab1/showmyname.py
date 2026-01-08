from sense_hat import SenseHat
import time

sense = SenseHat()

my_name = "Bhavaan Balasubramaniam"

text_color = [255, 255, 255]  
back_color = [0, 0, 0]       

print(f"Now scrolling '{my_name}' on the Sense HAT. Press Ctrl+C to stop.")

try:
    while True:
        sense.show_message(my_name, scroll_speed=0.08, text_colour=text_color, back_colour=back_color)
        time.sleep(1) 

except KeyboardInterrupt:
    sense.clear()
    print("\nScript stopped.")
