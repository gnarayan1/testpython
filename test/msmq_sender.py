'''
Created on Nov 16, 2014

@author: geeth
'''


import win32com.client
import os

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\GeethQueue"
queue=qinfo.Open(2,0)   # Open a ref to queue
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label="MyTest"
msg.Body = "Test123"
msg.Send(queue)

queue.Close()
