import sys

sys.path.append('C:/Users/Shiva/PycharmProjects/Raindrop')
import raindrop


def display(message):
    print message
raindrop.subscribe('mychannel', display)