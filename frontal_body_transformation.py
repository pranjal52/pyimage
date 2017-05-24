import cv2
class frontal_transformation:
	def _init_ (self, width = None, height = None):
		self.h = 0
		self.w = 0
		self.dim = None
		self.r = 0
		self.resized = None
		self.width= width
		self.height = height

	def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
		dim = None
		(h, w) = image.shape[:2]

		if width is None and height is None:
			return image

		if width is None:
			r = height / float(h)
			dim = (int(w * r), height)

		else:
			r = width / float(w)
			dim = (width, int(h * r))

		resized = cv2.resize(image, dim, interpolation = inter)
		return resized