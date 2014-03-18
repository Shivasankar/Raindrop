import socket
import json


def publish(channel, msg):
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host, port))
    sock.send(json.dumps({channel: msg}, separators=(',', ':'), sort_keys=True))


def subscribe(channel, fn):
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host,port))
    while True:
        sock.send(channel)
        msg = sock.recv(1024)
        fn(msg)