from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="C:/Selenium/Drivers/chromedriver_win32/chromedriver.exe")
        print("Launching chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:/Selenium/Drivers/geckodriver.exe")
        print("Launching firefox browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##############Pytest html report#############
#It is hook for adding environment info to HTML report

def pytest_configure(config):
    config._metadata['Project name'] = 'HybridFM'
    config._metadata['Module name'] = 'Login'
    config._metadata['Tester'] = 'Priya'

#It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)









