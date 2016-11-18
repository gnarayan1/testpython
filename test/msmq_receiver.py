'''
Created on Nov 16, 2014

@author: geeth
'''

import win32com.client
import os
#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='mytest')

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\GeethQueue"
queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)

while True:
    msg=queue.Receive()
    print("Label:",msg.Label)
    print("Body :",msg.Body)
    channel.basic_publish(exchange='',
                      routing_key=msg.Label,
                      body=msg.Body)

queue.Close()










