from PIL import Image
import numpy as np
def person_detected(image1_file,image2_file, t1):
    img1 = np.array(Image.open(image1_file).convert("L"))
    img2 = np.array(Image.open(image2_file).convert("L"))
    diff = np.abs(np.subtract(img1, img2))
    total_diff = np.sum(diff)
    print("Pixel difference value:", total_diff)
    return total_diff > t1
