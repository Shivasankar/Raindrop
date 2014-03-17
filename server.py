import socket
msg = ''


def socketconnect():
    s = socket.socket()
    host = socket.gethostname()
    port = 8777
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        channel = c.recv(1024)
        message = c.recv(1024)
        if message is None:
            while True:
                c.send(channel)
        print channel
        print msg
        dict = {channel: msg}
    return


socketconnect()
