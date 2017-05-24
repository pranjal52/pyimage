import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print ("width: %d pixels" % (image.shape[1]))
print ("height: %d pixels" % (image.shape[0]))
print ("channels: %d" % (image.shape[2]))
cv2.imshow("Image", image)
cv2.waitKey(0)

#cv2.imwrite("newabc.jpg", image)

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)