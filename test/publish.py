import sys
sys.path.append('C:/Users/Shiva/PycharmProjects/Raindrop')
import raindrop


def test(channel, msg):
    raindrop.publish(channel, msg)

test('Mychannel', 'sample text')
