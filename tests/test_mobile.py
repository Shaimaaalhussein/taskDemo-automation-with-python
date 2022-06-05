from pages.swagLabPage import swagLabPage
from mobileDriver_setup import mobileDriver


def test_mobile(mobileDriver):
# initilaize page objects
 swapLab_page=swagLabPage(mobileDriver)

# actions on mobile app
 swapLab_page.enterlogindata()
 swapLab_page.clickAddToCart()
 swapLab_page.clickCart()
 swapLab_page.clickCheckout()
 swapLab_page.enterCheckoutData()
 swapLab_page.clickFinish()
 assert "Your order has been dispatched" in swapLab_page.completeChekoutText()
