#coding=utf-8
import socket
from time import sleep
import time





class Tcpclient():




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



"""
if __name__ == '__main__':
    tcp = Tcpclient()
    tcp.tcpclient1('tag00001','771c11f656f94b568d55d665321ec1fc','Sensor0001')
"""

