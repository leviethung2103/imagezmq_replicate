## IMAGE ZMQ Library

Original repo is https://github.com/jeffbass/imagezmq

This repository is used to test the real scenario. 

## Installation

```
conda create --name imagezmq python=3.7
conda activate imagezmq
pip install imagezmq opencv-python 
```

## Testing

**Scenario 1: Test on local machine. The receiver is localhost**

The client and server are in the same network. 

**The sender** is receiving the streams from a camera through by RTSP protocol. Open the access for all connections at port 5555.

```bash
# Run the sender
python examples/pub_sub_broadcast.py 
# Run the server (receiver)
python examples/pub_sub_receive.py
```

The receiver is set up with hostname "127.0.0.1". Use the localhost.

> hostname = "127.0.0.1"

**Scenario 2: Test on local machine. The receiver is my public IP network**

All the configurations are the same as scenario 1. However, at this time, the localhost is changed into `"hunglv1994.ddns.net`, which is the DNS for the public IP of my local network. 

> hostname = "hunglv1994.ddns.net"