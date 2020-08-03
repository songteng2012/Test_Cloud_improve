#参考:https://blog.csdn.net/Likianta/article/details/90123678?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase

from time import sleep,time
import asyncio


def demo4():

    async def washing1():
        await asyncio.sleep(3)
        print('washer1 finished')
    """
    async def washing2():
        await asyncio.sleep(2)
        print('washer2 finished')

    """
    async def washing3():
        await washing1()
        print('washer3 finished')


    loop = asyncio.get_event_loop()


    tasks = [washing3(),]

    loop.run_until_complete(asyncio.wait(tasks))

    loop.close()


if __name__ == '__main__':
    start = time()
    demo4()
    end = time()
    print('elapsed time = ' + str(end - start))
