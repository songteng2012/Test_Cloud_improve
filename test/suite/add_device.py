import sys,os
path2add = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'page')))
if (not (path2add in sys.path)) :
    sys.path.append(path2add)
import unittest
from data.get_data import GetData
from ddt import ddt,data,unpack
from base_page import opera_click
from time import sleep
from utils.多线程 import Threads
import asyncio

@ddt
class NLE(unittest.TestCase):
    get_data = GetData(0)
    data_all = get_data.data()
    cloud = opera_click()
    L = []
    # tcp = Tcpclient()

    @classmethod
    def setUpClass(cls):
        cls.cloud.dr_get()

    @classmethod
    def tearDownClass(cls):
        cls.cloud.dr_quit()

    def setUp(self):
        self.cloud.cookie()

    @data(*data_all)
    @unpack
    def test_new_device(self,*args):
        if self.cloud.isElementExist('/html/body/header/div/nav/ul/li[5]/a') == True:
            #点击开发者中心按钮
            self.cloud.xpath_click('/html/body/header/div/nav/ul/li[5]/a')
            sleep(1)



        #点击新增项目按钮
        self.cloud.xpath_click('/html/body/div[1]/div/div[1]/div[1]/a')
        #切换到frame框架下
        self.cloud.loc_frame('myModalFrame')
        sleep(1)
        self.cloud.xpath_send_keys('//*[@id="Name"]',args[0])
        #点击"下一步"button按钮
        self.cloud.xpath_click('/html/body/div[1]/div/form/div[5]/div/input')


        #添加设备名称
        self.cloud.xpath_send_keys('//*[@id="Name"]',args[1])
        #添加设备标识符
        self.cloud.xpath_send_keys('//*[@id="Tag"]',args[2])
        #点击"确认添加设备",然后返回到"添加项目"页面
        self.cloud.xpath_click('/html/body/div/div/form/div[6]/div/input')
        """
        # #Bug:project_ID元素出现后，再去获取project_ID,对其显式等待
        self.cloud.show_wait("//span[@class='tag']")

        """
        #页面跳转到项目页面过程中会跳动导致获取不到元素,加上sleep(2)
        sleep(1)

        #获取project_ID
        project_ID = self.cloud.get_text("//span[@class='tag']")
        #点击链接进入添加设备页面
        projectid ="projectid-" + str(project_ID)
        path = "//*[@id=" + "'" + projectid + "'" +  "]/div/div/a[1]/div"
        self.cloud.xpath_click(path)

        #添加传感器和执行器
        #点击设备名称连接按钮,进入传感器页面
        self.cloud.xpath_click('//*[@id="list"]/tbody/tr/td[3]/a[1]')
        sleep(1)
        #点击"+"按钮添加传感器
        self.cloud.xpath_click('/html/body/div[1]/div/div[3]/div[1]/table/tbody/tr/td/a[2]')
        #切换到frame框架下
        self.cloud.loc_frame('myModalFrame')
        """
        #点击"自定义"标签,为了刷新一下，不然传感器名称可能输入不进去
        self.cloud.xpath_click('/html/body/ul/li[1]/a')
        """
        sleep(1)
        #添加传感器名称
        self.cloud.xpath_send_keys('//*[@id="Name"]',args[3])
        #添加传感器标识符
        self.cloud.xpath_send_keys('//*[@id="ApiTag"]',args[4])
        #点击"确认添加设备"
        self.cloud.xpath_click('/html/body/div/div/form/div[7]/div/input[1]')
        sleep(1)
        #点击"+"按钮添加执行器
        self.cloud.xpath_click('/html/body/div[1]/div/div[3]/div[2]/table/tbody/tr/td/a[2]')
        #切换到frame框架下
        self.cloud.loc_frame('myModalFrame')
        """
        #点击"自定义"标签,为了刷新一下，不然执行器名称可能输入不进去
        self.cloud.xpath_click('/html/body/ul/li[1]/a')
        """
        sleep(1)
        #添加执行器名称
        self.cloud.xpath_send_keys('//*[@id="Name"]',args[5])
        #添加执行器标识符
        self.cloud.xpath_send_keys('//*[@id="ApiTag"]',args[6])
        #选择单选按钮"开关型"
        self.cloud.addact_Sin_button(args[7])
        #点击"确认"
        self.cloud.xpath_click('/html/body/div/div/form/div[8]/div/input[1]')

        #页面跳转过程中会跳动导致获取不到元素,加上sleep(2)
        sleep(1)

        #获取SecretKey
        SecretKey = self.cloud.get_text("//td[@class='security-key']")
        #把device_tag,SecretKey,Sensor_tag放在一个元祖内
        T = ()
        T = (args[2],SecretKey,args[3])
        #把不同的元祖放在列表中
        self.L.append(T)
        #print(self.L)

        """
        #通过TCP连接方式上报数据
        self.tcp.tcpclient1(args[2],SecretKey,args[3])
        """

        """
        #Bug:"开发者中心"元素出现后，再去点击"开发者中心",对其显式等待
        self.cloud.show_wait('/html/body/header/div[2]/div/ol/li[2]/a')
        """
        #点击"开发者中心"返回到"添加项目页面"
        self.cloud.xpath_click('/html/body/header/div[2]/div/ol/li[2]/a')


    def test_tcpclient2(self):

        threads = Threads()
        threads.create_thread(self.L)


"""
if __name__ == '__main__':
    unittest.main(verbosity=2)
"""






