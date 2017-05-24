import numpy as np
import cv2
# canvas = np.ones((300, 300, 3), dtype = "uint8")

# green = (0, 255, 0)
# cv2.line(canvas, (0, 0), (300, 300), green, 3)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# red = (0, 0, 255)
# cv2.line(canvas, (300, 0), (0, 300), red, 3)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# cv2.rectangle(canvas, (50, 200), (200, 225), red, -1)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)
()
canvas1 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = ((int)(canvas1.shape[1] / 2), (int)(canvas1.shape[0] / 2))
white = (255, 255, 255)
r=25
cv2.circle(canvas1, (centerX, centerY), r, white)
cv2.imshow("Canvas1", canvas1)
cv2.waitKey(0)