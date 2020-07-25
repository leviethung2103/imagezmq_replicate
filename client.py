import socket
import time
from imutils.video import VideoStream
import imagezmq

# server_ip = '192.168.3.6'
server_ip  = 'hunglv1994.ddns.net'

sender = imagezmq.ImageSender(connect_to='tcp://{}:5555'.format(server_ip))

camera_name = 'EZVIZ'

# ezviz
ezviz = VideoStream(src='rtsp://admin:CFLPNX@192.168.3.68/h264_stream').start()

while True:
	image = ezviz.read()
	sender.send_image(camera_name,image)