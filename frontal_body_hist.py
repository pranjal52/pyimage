from matplotlib import pyplot as plt
import argparse
import cv2
class frontal_hist:
	def show_hist (image, bins = 256):
		hist = cv2.calcHist([image], [0], None, [bins], [0, bins])

		plt.figure()
		plt.title("Grayscale Histogram")
		plt.xlabel("Bins")
		plt.ylabel("# of Pixels")
		plt.plot(hist)
		plt.xlim([0, bins])
		plt.show()
		cv2.waitKey(0)
	
	def equalize_hist (image):
		return (cv2.equalizeHist(image))
		
	