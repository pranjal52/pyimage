from frontal_body_transformation import frontal_transformation
from frontal_body_hist import frontal_hist
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "path to where the image file resides")
args = vars(ap.parse_args())

#showing raw image
image = cv2.imread(args["image"])
cv2.imshow("Raw", image)
cv2.waitKey(0)

#resizing of image
resized_image = frontal_transformation.resize(image, width = 400)

#showing resized image
cv2.imshow("Resized", resized_image)
cv2.waitKey(0)

#grayscaling the image
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#showing grayscaled image
cv2.imshow("Grayscaled", gray)
cv2.waitKey(0)

#showing grayscale histogram
frontal_hist.show_hist(gray)

#equalizing histogram
eq_gray = frontal_hist.equalize_hist(gray)
cv2.imshow("Equalized Image", eq_gray)
cv2.waitKey(0)
frontal_hist.show_hist(eq_gray)

