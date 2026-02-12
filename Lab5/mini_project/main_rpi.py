from helper_functions import camera, computer_vision, sensehat
import time
import os

BACKGROUND_PATH = "data/images/background.jpg"


def countdown(seconds, message=""):
    if message:
        print(message)
    for i in range(seconds, -1, -1):
        print(i)
        time.sleep(1)


def main():
    camera_i = camera.get_camera()  # DO NOT MODIFY
    sense = sensehat.get_sensehat()  # DO NOT MODIFY

    while True:
        print("\n--- Home Security System ---")
        print("1 - Background already saved")
        print("2 - Take background image")
        print("3 - Arm system")
        print("4 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            if os.path.exists(BACKGROUND_PATH):
                print("Background image found.")
            else:
                print("Background image NOT found. Choose option 2 to take one.")

        elif choice == "2":
            print("Get out of the scene")
            countdown(10, "Background image will be taken in 10 seconds...")
            camera.capture_image(camera_i, BACKGROUND_PATH, countdown_time=0, preview=False)
            print("Background image saved.")

        elif choice == "3":
            if not os.path.exists(BACKGROUND_PATH):
                print("ERROR: No background image found. Choose option 2 first.")
                continue

            interval = int(input("Enter interval between test images (seconds): "))
            t1 = int(input("Enter threshold t1: "))

            countdown(10, "Monitoring will begin in 10 seconds...")

            count = 0
            while True:
                image_path = f"data/images/image{count}.jpg"
                camera.capture_image(camera_i, image_path, countdown_time=interval)
                person_detected = computer_vision.person_detected(
                    BACKGROUND_PATH, image_path, t1
                )

                if person_detected:
                    print("Person Detected")
                    sensehat.alarm(sense, interval)
                else:
                    print("No Person Detected")

                count += 1

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
