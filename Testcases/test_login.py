
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepagetitle(self,setup):

        self.logger.info("******* Test_001_Login ******")
        self.logger.info("****** Verify homepagetitle ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title== "Login":
            assert True
            self.driver.close()
            self.logger.info("******* Title Passed ******")
        else:
            self.driver.close()
            self.logger.error("******* Title Failed ******")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(8)
        self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")
        self.lp.click_logout()
        self.driver.close()


