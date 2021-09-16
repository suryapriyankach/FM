import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddUserPage import Adduser

class Test_003_Adduser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_adduser(self, setup):
        self.logger.info("******* Test_003_Login ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(8)
        self.logger.info("******Login successfull*******")
        self.logger.info("*******Starting add user****")

        self.adusr = Adduser(self.driver)
        self.adusr.click_settingstile()
        self.adusr.click_usermngmnttile()
        self.adusr.click_userstile()

        self.logger.info("*******Providing user info*******")

        self.usr = random_generator()
        self.adusr.enter_username(self.usr)
        self.adusr.enter_password("12345")
        self.adusr.enter_confirmpassword("12345")

        self.email = random_generator() + '@gmail.com'
        self.adusr.enter_emailid(self.email)
        self.adusr.enter_realname("PriyaPraveen")
        self.adusr.click_savebtn()
        time.sleep(5)


        self.logger.info("********** saving user info*********")
        self.logger.info("******** Add user validation started*********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'New user added' in self.msg:
            assert True
            self.logger.info("******* add user passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_adduser.png")
            self.logger.info("******* add user failed***********")
            assert False

        self.adusr.click_closebtn()
        self.lp.click_logout()
        self.driver.close()



def random_generator(size=5, chars=string.ascii_lowercase):
    return''. join(random.choice(chars) for x in range(size))












