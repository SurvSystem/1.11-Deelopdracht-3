#!/usr/bin/python2.7
import socket
import datetime
import telepot
import time
import requests
import os
import glob
import telebot
from telepot.loop import MessageLoop


x = datetime.datetime.now()
telegramUserId1 = 888317203 #Telegram ID van mij


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # testen of er verbinding is met dns van google
local_ip_address = s.getsockname()[0]


def webcontrol(chat_id, type, cmd):
    req = 'http://localhost:8080/0/'+type+'/'+cmd
    res = requests.get(req)
    bot.sendMessage(chat_id, res.text)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #zorgen ervoor dat er 1 iemand toegang heeft.
    if msg['from']['id'] != telegramUserId1:
        bot.sendMessage(chat_id, "Sorry dit is een persoonlijke bot. Toegang geweigerd!")
        exit(1)
   

    print 'Got command: %s' % command

    if command == '/snapshot':
        requests.get('http://localhost:8080/0/action/snapshot')
    elif command == '/status':
        webcontrol(chat_id, 'detection', 'status')
    elif command == '/pauze':
        webcontrol(chat_id, 'detection', 'pause')
    elif command == '/verder':
        webcontrol(chat_id, 'detection', 'start')
    elif command == '/check':
        webcontrol(chat_id, 'detection', 'connection')
    elif command == '/datum':
        bot.sendMessage(chat_id, 'Het is nu '+str(x.strftime("%x")))
    elif command == '/tijd':
        bot.sendMessage(chat_id, 'Het is nu '+str(x.strftime("%X")))
    elif command == '/start':
        bot.sendMessage(chat_id, 'Welkom bij Surv System')
    elif command == '/ip':
        bot.sendMessage(chat_id, 'Hierbij uw Local IP-adres: ' + local_ip_address)  
    elif command == '/livekijken':
        bot.sendMessage(chat_id,'Klik op de volgende adress om live te bekijken: http://' + local_ip_address + ':8081')
    elif command == '/video':
        # laatste video uit het folder vis
        video = max(glob.iglob('/home/pi/motion/detected/vids/*.mp4'), key=os.path.getctime)
        # sturen van die video
        bot.sendVideo(888317203, video=open(video, 'rb'), caption='Hierbij het laatste video!')
    
    else:
        bot.sendMessage(chat_id, "sorry, deze command ken ik niet -> "+command)
# bot token
bot = telepot.Bot('1086113653:AAFcTV4L5IDYyULa0ElhDcg4YfrTN73hhpI')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
