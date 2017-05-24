from face_detector import FaceDetector
import argparse
import cv2

#defining  a function for resizing image
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




ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "path to where the face cascade resides")
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

if not args.get("video", False):
	camera = cv2.VideoCapture(0)

else:
	camera = cv2.VideoCapture(args["video"])

while True:
	(grabbed, frame) = camera.read()

	if args.get("video") and not grabbed:
		break

	frame = resize(frame, width = 400)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faceRects = fd.detect(gray, scaleFactor = 1.25, minNeighbors = 3, minSize = (5, 5))
	frameClone = frame.copy()

	for (fX, fY, fW, fH) in faceRects:
		cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),(0, 255, 0), 2)

	cv2.imshow("Face", frameClone)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()