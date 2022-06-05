from typing import List, Any

from selenium.webdriver.common.by import By
from configuration import configurationReader
from configuration import configFile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basePage:

    def __init__(self, broswer):
        self.browser = broswer


        wait = WebDriverWait(self.browser, 60)

    # Open website
    def openWebsite(self):
        webURL = configurationReader.get_web_url()
        self.browser.get(webURL)

    # get current url
    def getCurrentURL(self,text):
        WebDriverWait(self.browser, 70).until(EC.url_contains(text))
        return self.browser.current_url

    # click element
    def clickElementByXpath(self, elementBy):
        element = WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, elementBy)))
        self.browser.execute_script("arguments[0].click();", element)

    # get array of element
    def getArrayText(self, elementBy):
        textString = []
        elements = WebDriverWait(self.browser, 60).until(
                EC.presence_of_all_elements_located((By.XPATH, elementBy)))
        for element in elements:
            textString.append(element.text)
        return textString

    # get text of element
    def getText(self, elementBy):
        element = WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, elementBy)))
        return element.text





