from pages.mobileBasePage import mobileBasePage

class swagLabPage:

  # locators
  username="test-Username"
  password="test-Password"
  loginBtn ="test-LOGIN"
  addToCart = "(//android.view.ViewGroup[@content-desc=\"test-ADD TO CART\"])[1]"
  cart = "//android.view.ViewGroup[@content-desc=\"test-Cart\"]/android.view.ViewGroup/android.widget.ImageView"
  checkout = "test-CHECKOUT"
  firstname="test-First Name"
  lastname="test-Last Name"
  postalcode="test-Zip/Postal Code"
  continueBtn="test-CONTINUE"
  finish="test-FINISH"
  completeCheckout='//android.widget.ScrollView[@content-desc="test-CHECKOUT: COMPLETE!"]/android.view.ViewGroup/android.widget.TextView[2]'

  def __init__(self,mobileDriver):
   self.browser=mobileDriver
   self.mobileBase_Page = mobileBasePage(self.browser)

  # enter login data
  def enterlogindata(self):
       self.browser.implicitly_wait(10)
       self.mobileBase_Page.enterValue(self.username,"standard_user")
       self.mobileBase_Page.enterValue(self.password,"secret_sauce")
       self.mobileBase_Page.clickByAccessID(self.loginBtn)


  # click add to cart
  def clickAddToCart(self):
      self.mobileBase_Page.clickByXpath(self.addToCart)

  # click cart
  def clickCart(self):
      self.mobileBase_Page.clickByXpath(self.cart)

  # click checkout
  def clickCheckout(self):
      self.mobileBase_Page.clickByAccessID(self.checkout)

  # enter checkout data
  def enterCheckoutData(self):
      self.mobileBase_Page.enterValue(self.firstname,"shaimaa")
      self.mobileBase_Page.enterValue(self.lastname, "alhussein")
      self.mobileBase_Page.enterValue(self.postalcode, "67")
      self.mobileBase_Page.clickByAccessID(self.continueBtn)
  #click finish
  def clickFinish(self):
      self.mobileBase_Page.scrollByText("FINISH")
      self.mobileBase_Page.clickByAccessID(self.finish)

  # complete checkout
  def completeChekoutText(self):
      self.browser.implicitly_wait(6)
      return self.mobileBase_Page.getTextXpath(self.completeCheckout)

