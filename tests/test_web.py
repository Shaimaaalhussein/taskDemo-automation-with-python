"""
This module contains basic web tests
check on several languages
"""
#-----------------------------------------------------------------------------------------------
#imports
#-----------------------------------------------------------------------------------------------

from browser_setup import browser
from pages.homePage import homePage
from pages.basePage import basePage
from pages.startManagePage import startManagePage
#-----------------------------------------------------------------------------------------------
#tests
#-----------------------------------------------------------------------------------------------

def test_web_en(browser):
# initilaize page objects
        base_Page=basePage(browser)
        home_page=homePage(browser)
        startManage_page=startManagePage(browser)
# actions on website
        base_Page.openWebsite()
        home_page.clickStartAndManage()
        # Assert start and manage page opened
        assert "Start-and-Manage" in base_Page.getCurrentURL("Start-and-Manage")
        startManage_page.clickStebByStep()
        # Assert user guide page opened
        assert "user-guide" in base_Page.getCurrentURL("user-guide")
# Assert first question
        assert "What would you like to do?" in startManage_page.getTextofQuestion()
        startManage_page.selectFirstAnswer()
        startManage_page.clickNext()
        assert "Are you planning to open a new company?" in startManage_page.getTextofQuestion()
        assert "Get a licence now" in startManage_page.getTextofPreviousAnswers()
        startManage_page.selectThirdAnswer()
        startManage_page.clickNext()
        assert "Where is your main business located?" in startManage_page.getTextofQuestion()
        assert "Get a licence now" in startManage_page.getTextofPreviousAnswers()
        assert "No, I want to open a branch for my existing business." in startManage_page.getTextofPreviousAnswers()
        startManage_page.selectFirstAnswer()
        startManage_page.clickNext()
        assert "login" in base_Page.getCurrentURL("login")
        print("test pass")

def test_web_ar(browser):
# initilaize page objects
        base_Page=basePage(browser)
        home_page=homePage(browser)
        startManage_page=startManagePage(browser)
# actions on website
        base_Page.openWebsite()
        home_page.changeLanguage()
        home_page.clickStartAndManage()
        # Assert start and manage page opened
        assert "Start-and-Manage" in base_Page.getCurrentURL("Start-and-Manage")
        startManage_page.clickStebByStep()
        # Assert user guide page opened
        assert "user-guide" in base_Page.getCurrentURL("user-guide")
# Assert first question
        assert "ما الذي ترغب بفعله؟" in startManage_page.getTextofQuestion()
        startManage_page.selectFirstAnswer()
        startManage_page.clickNext()
        assert "هل تخطط لفتح شركة جديدة؟" in startManage_page.getTextofQuestion()
        assert "أرغب بالحصول على رخصة الآن" in startManage_page.getTextofPreviousAnswers()
        startManage_page.selectThirdAnswer()
        startManage_page.clickNext()
        assert "أين يقع مقر شركتك الرئيسي؟" in startManage_page.getTextofQuestion()
        assert "أرغب بالحصول على رخصة الآن" in startManage_page.getTextofPreviousAnswers()
        assert "لا، أرغب بفتح فرع لشركتي القائمة." in startManage_page.getTextofPreviousAnswers()
        startManage_page.selectFirstAnswer()
        startManage_page.clickNext()
        assert "login" in base_Page.getCurrentURL("login")
        print("test pass")

