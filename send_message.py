#!/usr/bin/python2.7

import telepot
import sys

bot = telepot.Bot('1086113653:AAFcTV4L5IDYyULa0ElhDcg4YfrTN73hhpI')

text = sys.argv[1]

bot.sendMessage(888317203, text)
