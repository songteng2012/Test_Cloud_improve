#coding=utf-8
import socket
from time import sleep
import time
import threading

#from test.suite.add_device import NLE

class Threads():


    def tcpclient1(self,device_tag,SecretKey,Sensor_tag):

        time_format = '%Y-%m-%d %X'
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('117.78.1.201',8600))
        bdevice_tag = device_tag.encode()
        bSecretKey = SecretKey.encode()
        bconnect_cmd = b'{"t":1,"device":"' + bdevice_tag + b'","key":"' + bSecretKey + b'","ver":"v1.3"}\r'
        s.send(bconnect_cmd)
        bSensor_tag = Sensor_tag.encode()
        while True:
            current_time = time.strftime(time_format,time.localtime())
            bcurrent_time = current_time.encode()
            bdata_cmd = b'{"t":3,"datatype":2,"datas":{"' + bSensor_tag + b'":{"' + bcurrent_time + b'":22.5}},"msgid":123}\r'
            s.send(bdata_cmd)
            sleep(3)
            continue


    def create_thread(self,l):

        num = range(len(l))
        threads = []
        #创建多个线程
        for tup in l:
            t = threading.Thread(target=self.tcpclient1,args=tup)
            threads.append(t)

        for t in num:
            threads[t].start()
        for t in num:
            threads[t].join()
        #主线程
        print('Over')

