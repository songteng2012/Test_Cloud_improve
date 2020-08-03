#参考:廖雪峰python官网
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio
from time import sleep

async def hello1():
    print('Hello world0! (%s)' % threading.currentThread())
    print('Hello world1! (%s)' % threading.currentThread())
    await hello3()


async def hello2():
    print('Hello worlda! (%s)' % threading.currentThread())
    print('Hello worldb! (%s)' % threading.currentThread())
    await hello3()


async def hello3():
    while True:
        print('Hello again! (%s)' % threading.currentThread())
        sleep(3)
        continue


loop = asyncio.get_event_loop()
tasks = [hello1(),hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()