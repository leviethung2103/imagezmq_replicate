import cv2
import imagezmq 
from datetime import datetime

# initialize the ImageHub object
print ("[INFO] Starting server")
image_hub = imagezmq.ImageHub()

lastActive = {}
lastActiveCheck = datetime.now()

while True:
	device_name, image = image_hub.recv_image()
	image_hub.send_reply(b'OK')
	

	if device_name not in lastActive.keys():
		print (f"[INFO] Receiving data from {device_name}")

	# record the last active time for the device from which we just 
	# recevied a frame
	lastActive[device_name] = datetime.now()


	cv2.imshow(device_name,image) 
	cv2.waitKey(1)



