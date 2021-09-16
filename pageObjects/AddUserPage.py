from selenium.webdriver.common.by import By


class Adduser:
    tile_settings_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[3]"
    tile_usermanagement_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[1]"
    tile_users_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[3]/div[1]"

    new_user_dropdown_id = "UserDropDownList"
    txtbox_username_xpath = "//input[@id='UserNameBox']"
    txtbox_password_xpath = "//input[@id='PasswordBox']"
    txtbox_confirm_password_id = "ConfirmBox"
    txtbox_emailid_id = "EmailBox"
    txtbox_realname_id = "RealNameBox"

    btn_save_xpath = "//body/div[@id='mainPage']/div[@id='pageContent']/div[1]/div[2]/div[1]/input[1]"
    btn_popup_xpath = "//a[@id='popupMessageCloseButton']"

    def __init__(self, driver):
        self.driver = driver

    def click_settingstile(self):
        self.driver.find_element(By.XPATH,self.tile_settings_xpath).click()

    def click_usermngmnttile(self):
        self.driver.find_element(By.XPATH, self.tile_usermanagement_xpath).click()

    def click_userstile(self):
        self.driver.find_element(By.XPATH, self.tile_users_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.txtbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def enter_confirmpassword(self, confirmpassword):
        self.driver.find_element(By.ID, self.txtbox_confirm_password_id).clear()
        self.driver.find_element(By.ID, self.txtbox_confirm_password_id).send_keys(confirmpassword)

    def enter_emailid(self, emailid):
        self.driver.find_element(By.ID, self.txtbox_emailid_id).clear()
        self.driver.find_element(By.ID, self.txtbox_emailid_id).send_keys(emailid)

    def enter_realname(self, realname):
        self.driver.find_element(By.ID, self.txtbox_realname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_realname_id).send_keys(realname)

    def click_savebtn(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def click_closebtn(self):
        self.driver.find_element(By.XPATH, self.btn_popup_xpath).click()
        

