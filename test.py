#!/usr/bin/python2.7

import telepot
import sys

bot = telepot.Bot('1086113653:AAFcTV4L5IDYyULa0ElhDcg4YfrTN73hhpI')


cap = 'test.'

bot.sendMessage(888317203, caption=cap)

exit(0)