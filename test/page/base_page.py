from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    def __init__(self):
        self.driver = webdriver.Chrome()


    def dr_get(self):
        self.base_url = "http://www.nlecloud.com"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)


    def dr_quit(self):
        self.driver.refresh()
        self.driver.quit()

    def cookie(self):
        self.driver.add_cookie({'name':'NECAUTH','value':'NECAUTH_ETS=2020-07-05+09%3a13%3a50&UserID=75318&Username=&Email=&Telphone=18668102621&Gender=True&CollegeID=0&CollegeName=&RoleID=15&RoleName=%e6%99%ae%e9%80%9a%e4%bc%9a%e5%91%98&EN=46cf87b6f73ff2ce'})
        self.driver.refresh()


class opera_click(BasePage):

    def loc_frame(self,frame):
         self.driver.switch_to.frame(frame)

    def xpath_click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()


    def xpath_send_keys(self,xpath,str):
        self.driver.find_element_by_xpath(xpath).send_keys(str)


    def sel_list(self,num):
        m = self.driver.find_element_by_xpath('//*[@id="Industry"]')
        m.find_element_by_xpath('//*[@id="Industry"]/option['+ str(num) +']').click()

    def newproject_Sin_button(self,num):
        self.driver.find_element_by_xpath('/html/body/div/div/form/div[3]/div/div[' + str(num) + ']/label/div/ins').click()

    def adddevice_Sin_button(self,num):
        self.driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[' + str(num) + ']').click()

    def addact_Sin_button(self,num):
        self.driver.find_element_by_xpath('/html/body/div/div/form/div[6]/div/div[' + str(num) + ']/label/div/ins').click()

    #判断元素是否存在
    def isElementExist(self,element):
        flag = True
        try:
            self.driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    #提取文本元素
    def get_text(self,xpath):
        text = self.driver.find_element_by_xpath(xpath).text
        return text

    #显式等待
    def show_wait(self,xpath):
        WebDriverWait(self.driver,10,0.5).until(lambda e1: self.driver.find_element_by_xpath(xpath))


