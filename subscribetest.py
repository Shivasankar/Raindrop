import sys

sys.path.append('C:/Users/Shiva/PycharmProjects/sample2')
import sample2
channel = 'my_channel'
message = ''
fn = 'subscribe'

def subscribe(channel, fn):
    sample2.subscribe(channel, fn)
    return message


fn = subscribe(channel, fn)
print message
