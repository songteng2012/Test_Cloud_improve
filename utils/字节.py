import time

time_format = '%Y-%m-%d %X'
current_time = time.strftime(time_format,time.localtime())
print(current_time)
print(type(current_time))




print(current_time.encode())