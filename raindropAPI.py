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


def subscribe(channel, fn):
    message = 'shiva msg from sample2'
    function = fn
    for message in channel:
        function(message)
    return function(message)
