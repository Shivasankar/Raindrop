import sys

sys.path.append('C:/Users/Shiva/PycharmProjects/sample2')
import sample2
channel = 'my_channel'
message = ''

def subscribe(channel):
    sample2.subscribe(channel)
    return message


fn = subscribe(channel)
print message
