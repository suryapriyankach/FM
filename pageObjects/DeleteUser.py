from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Deleteuser:
    drpdwn_click_xpath = "//select[@id='UserDropDownList']"
    btn_delete_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[2]/div[3]/input[1]"
    btn_ok_xpath = "//a[@id='popupConfirmOk']"
    btn_close_xpath = "//a[@id='popupMessageCloseButton']"

    def __init__(self, driver):
        self.driver = driver

    def click_dropdown(self, name):
        self.driver.find_element(By.XPATH, self.drpdwn_click_xpath).click()

    def click_delete_btn(self):
        self.driver.find_element(By.XPATH, self.btn_delete_xpath).click()

    def click_ok_btn(self):
        self.driver.find_element(By.XPATH, self.btn_ok_xpath).click()

    def click_close_btn(self):
        self.driver.find_element(By.XPATH, self.btn_close_xpath).click()







