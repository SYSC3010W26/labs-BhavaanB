from sense_hat import SenseHat
import time
def get_sensehat():
    return SenseHat()


# This function takes in a SenseHat instance and the flash_time
# The display on the SenseHat flashes red (1 second on, 1 second off) for the duration of flash_time. At the end of the flash_time the SenseHat display should be off.
def alarm(sense,flash_time):
    red = (255, 0, 0)
    off = (0, 0, 0)
    end_time = time.time() + flash_time
    while time.time() < end_time:
        sense.clear(red)
        time.sleep(1)
        sense.clear(off)
        time.sleep(1)
    sense.clear()