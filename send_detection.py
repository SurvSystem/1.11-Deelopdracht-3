#!/usr/bin/python2.7

import telepot
import sys

bot = telepot.Bot('1086113653:AAFcTV4L5IDYyULa0ElhDcg4YfrTN73hhpI')

pic = sys.argv[1]

# bepaalt of het een snapshot of een beweging is.
if pic.endswith("snapshot.jpg"):
    cap = 'Een snapshot.'
else:
    cap = 'Er is beweging gedecteerd.'

bot.sendPhoto(888317203, photo=open(pic, 'rb'), caption=cap)

exit(0)
