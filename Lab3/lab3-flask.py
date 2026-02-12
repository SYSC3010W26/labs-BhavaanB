from flask import Flask, render_template
from flask_socketio import SocketIO
from sense_hat import SenseHat
import json

sense = SenseHat()

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def send_current_colors():
    colors = sense.get_pixels()  
    packet = json.dumps({"colors": colors})
    socketio.emit("current_colors", packet)

@socketio.on("update_led")
def update_led(data):
    packet = json.loads(data)
    led_id = int(packet["id"])
    color_hex = packet["color"]

    r = int(color_hex[1:3], 16)
    g = int(color_hex[3:5], 16)
    b = int(color_hex[5:7], 16)

    sense.set_pixel(led_id // 8, led_id % 8, (r, g, b))

    socketio.emit("update_led", data)

@socketio.on("clear_leds")
def clear_leds():
    print("Clear LEDs event received")
    sense.clear()

    # Send updated (all black) colors back to browser
    colors = sense.get_pixels()
    packet = json.dumps({"colors": colors})
    socketio.emit("current_colors", packet)


if __name__ == "__main__":
    print("Flask server starting...")
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
