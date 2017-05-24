import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)



blurred = cv2.medianBlur(image, 3)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
blurred = cv2.medianBlur(image, 7)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)