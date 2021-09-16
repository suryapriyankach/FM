import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.DeleteUser import Deleteuser
from pageObjects.AddUserPage import Adduser

class Test_004_Deltuser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_deleteuser(self, setup):
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
        self.logger.info("*******Starting delete user****")

        self.adusr = Adduser(self.driver)
        self.adusr.click_settingstile()
        self.adusr.click_usermngmnttile()
        self.adusr.click_userstile()

        self.delusr = Deleteuser(self.driver)
        self.delusr.click_dropdown()

        self.delusr.click_delete_btn()
        time.sleep(5)
        self.delusr.click_ok_btn()

        self.lp.click_logout()
        self.driver.close()




