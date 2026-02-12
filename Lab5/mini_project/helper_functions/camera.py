from picamera2 import Picamera2
import time
def get_camera():
    camera = Picamera2()
    return camera
def camera_preview(camera, preveiw_time):
    camera.start_preview()
    time.sleep(preview_time)
    camera.stop_preview()
def capture_image(camera,image_out_location, countdown_time = 0, preview = False ):
    if preview: camera.start_preview()
    for i in range(countdown_time, 0, -1):
        print(i)
        time.sleep(1)
    camera.capture_file(image_out_location)
    if preview:
        camera.stop_preview()
def capture_video(camera,video_out_location, video_length, countdown_time = 0, preview = False):
    if preview: camera.start_preview()
    for i in range(countdown_time, 0, -1):
        print(i)
        time.sleep(1)
    camera.start_recording(video_out_location)
    time.sleep(video_length)
    camera.stop_recording()
    if preview:
        camera.stop_preview()
