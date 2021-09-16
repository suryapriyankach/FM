from selenium.webdriver.common.by import By


class Login:
    textbox_Username_id = "UserName"
    textbox_Password_id = "Password"
    button_Login_xpath = "/html/body/div[1]/div[2]/div/form/div/ul/li[4]/table/tbody/tr/td/div/input"
    button_Logout_xpath = "//a[@id='logoffbutton']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_Username_id).clear()
        self.driver.find_element(By.ID, self.textbox_Username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_id).clear()
        self.driver.find_element(By.ID, self.textbox_Password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()


