import socket
import json


def publish(channel, msg):
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host, port))
    request_type = 'p'
    sock.send(json.dumps(({channel: msg}, request_type), separators=(',', ':'), sort_keys=True))


def subscribe(channel, fn):
    request_type = 's'
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host,port))
    while True:
        sock.send(json.dumps({channel, request_type}, separators=(',', ':')))
        msg = sock.recv(1024)
        fn(msg)