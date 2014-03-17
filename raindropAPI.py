import socket


def publish(channel, msg):
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host, port))
    channel = channel
    message = len(msg)
    while message != 0:
        sock.send((channel, msg))
    return channel, msg


def subscribe(channel):
    sock = socket.socket()
    port = 8777
    host = socket.gethostname()
    sock.connect((host,port))
    while True:
        sock.send(channel)
        message = sock.recv(1024)
    for message in channel:
        msg = message
    return msg
