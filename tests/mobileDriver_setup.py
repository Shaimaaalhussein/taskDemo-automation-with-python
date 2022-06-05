import pytest
from appium import webdriver
from configuration import configurationReader
from configuration import configFile

@pytest.fixture
def mobileDriver():

  desired_caps = configurationReader.get_mobile_cap()

  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
  return driver

  driver.quit()