import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


def load_images():
    file_names = os.listdir("images")
    file_names = ["images\{}".format(name) for name in file_names]

    images =list()
    cropped_images= list()
    for file_name in file_names:
        image = cv2.imread(file_name)
        cropped_image= image[50:550,130:650]
        images.append(image)
        cropped_images.append(cropped_image)
        # print(image.shape)
    return cropped_images


def show_image(image):
    plt.imshow(image)
    plt.show()


def blob_detection(image):
    detector = cv2.SimpleBlobDetector()
    


images = load_images()
focus = images[0]

