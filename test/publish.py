import sys

sys.path.append('C:/Users/Shiva/PycharmProjects/sample2')
import sample2

msg = "sample text"
channel = "Mychannel"


def publish(channel, msg):
    info = sample2.publish(channel, msg)
    print info
    return channel, msg


publish(channel, msg)
print channel
print msg
