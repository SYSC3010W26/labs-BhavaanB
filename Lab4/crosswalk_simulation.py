from time import sleep
from gpiozero import Button
from traffic_lights import TrafficLights

RED = 5
YELLOW = 6
GREEN = 16
BUTTON = 26

def main():
    color = TrafficLights(RED, YELLOW, GREEN)
    button = Button(BUTTON, pull_up=True)

    state = "RED"

    while True:
        if state == "RED":
            color.red_on()
            sleep(5)
            state = "GREEN"

        elif state == "GREEN":
            color.green_on()
            pressed = button.wait_for_press(timeout=5)
            state = "YELLOW"

        elif state == "YELLOW":
            color.yellow_on()
            sleep(2)
            state = "RED"

if __name__ == "__main__":
    main()
