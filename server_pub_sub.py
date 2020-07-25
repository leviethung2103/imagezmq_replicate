import cv2
import imagezmq 
from datetime import datetime


print ("[INFO] Starting server")
image_hub = imagezmq.ImageHub(open_port='tcp://192.168.3.6:5555',REQ_REP=False)

# specify the address for every sender
image_hub.connect('tcp://192.168.3.21:5555')


while True:
	device_name, image = image_hub.recv_image()
	if device_name:
		print (device_name)
		print (image.shape)
		cv2.imshow(device_name,image) 
		cv2.waitKey(1)



