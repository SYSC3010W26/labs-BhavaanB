from time import sleep
from traffic_lights import TrafficLights

RED = 5
YELLOW = 6
GREEN = 16

def main():
    tl = TrafficLights(RED, YELLOW, GREEN)

    tl.red_on()
    sleep(0.2)
    assert tl.red.value == 1
    assert tl.yellow.value == 0
    assert tl.green.value == 0

    tl.yellow_on()
    sleep(0.2)
    assert tl.red.value == 0
    assert tl.yellow.value == 1
    assert tl.green.value == 0

    tl.green_on()
    sleep(0.2)
    assert tl.red.value == 0
    assert tl.yellow.value == 0
    assert tl.green.value == 1

    print("All tests passed.")

if __name__ == "__main__":
    main()
