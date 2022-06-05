from pages.basePage import basePage

class homePage:

  # locators
  start="//a[contains(@href,'Start-and-Manage')]//div[@class='link-inside']"
  arabicLanguage="//a[@href='/ar-AE']"
  def __init__(self,broswer):
   self.browser=broswer
   self.base_page = basePage(self.browser)

  # Click start and manage
  def clickStartAndManage(self):
       self.base_page.clickElementByXpath(self.start)

 # Click start and manage
  def changeLanguage(self):
       self.base_page.clickElementByXpath(self.arabicLanguage)

