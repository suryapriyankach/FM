
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testdata/Testdata.xlsx"
    logger = LogGen.loggen()


    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a excel:", self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            time.sleep(8)
            #self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")

            if self.exp=="pass":
                self.logger.info("*****Passed*****")
                self.lp.click_logout()
                lst_status.append("Pass")
            elif self.exp=="fail":
                self.logger.info("********Failed*******")
                lst_status.append("Fail")

        if "fail" not in lst_status:
            self.logger.info("****DDT is passed*********")
            self.driver.close()
            assert True

        else:
            self.logger.info("****DDT is failed********")
            self.driver.close()
            assert False

        self.logger.info("*********End of Login DDT*********" )
        self.logger.info("***********Completed********")






