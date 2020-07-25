import cv2



CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

PROTOTXT = 'models/MobileNetSSD_deploy.prototxt'
MODEL_PATH = 'models/MobileNetSSD_deploy.caffemodel'

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL_PATH)


CONSIDER = set(["person"])
objCount = {obj: 0 for obj in CONSIDER}
frameDict = {}