#参考:https://www.cnblogs.com/xinghun85/p/9937741.html

import time
import asyncio
import requests

async def test2(i):
    r = await other_test(i)
    print(i,r)


async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    print(time.time()-start)
    return r


url = ["https://segmentfault.com/p/1210000013564725","https://www.jianshu.com/p/83badc8028bd","https://www.baidu.com/"]


loop = asyncio.get_event_loop()

tasks = [asyncio.ensure_future(test2(i)) for i in url]

start = time.time()

loop.run_until_complete(asyncio.wait(tasks))

endtime = time.time()-start
print(endtime)
loop.close()