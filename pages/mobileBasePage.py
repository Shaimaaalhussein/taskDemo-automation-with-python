from typing import List, Any
from appium.webdriver.common.appiumby import AppiumBy
from configuration import configurationReader
from configuration import configFile



class mobileBasePage:

    def __init__(self, mobileDriver):
        self.driver = mobileDriver


    # click by accessibilty ID
    def clickByAccessID(self,elementAccessID):
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=elementAccessID)
        el.click()


    # click by xpath
    def clickByXpath(self, elementXpath):
        el = self.driver.find_element(by=AppiumBy.XPATH, value=elementXpath)
        el.click()

    # getText by xpath
    def getTextXpath(self, elementXpath):
        el = self.driver.find_element(by=AppiumBy.XPATH, value=elementXpath)
        return el.text

    # getText by access ID
    def getTestAccessID(self, elementAccessID):
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=elementAccessID)
        return el.text

    # enter value
    def enterValue(self, elementAccessID,text):
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=elementAccessID)
        el.send_keys(text)

    #scroll by text
    def scrollByText(self,text):
        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\""+text+"\").instance(0));")
