from pages.basePage import basePage


class startManagePage:
    # locators
    stepBystep = "//a[contains(@href,'user-guide')]"
    question = "//h3[@class='ui-lib-questionnaire-question__title']"
    answer = "//input[contains(@id,'uil_radio_button')]"
    firstAnswer = "(//input[contains(@id,'uil_radio_button')])[1]"
    thirdAnswer = "(//input[contains(@id,'uil_radio_button')])[3]"
    nextBtn = "//button[contains(@class,'ui-lib-button qa-button ui-lib-button_primary ui-lib-button_default')]"
    previousAnswers = "//div[@class='ui-lib-questionnaire-answer__content-text']"
    loginElement = "//div[@class='ui-lib-login-required']"

    # constructor
    def __init__(self, broswer):
        self.browser = broswer
        self.base_page = basePage(self.browser)

    # Click step by step
    def clickStebByStep(self):
        self.base_page.clickElementByXpath(self.stepBystep)

    # select first answer

    def selectFirstAnswer(self):
        self.base_page.clickElementByXpath(self.firstAnswer)

    # select third answer
    def selectThirdAnswer(self):
        self.base_page.clickElementByXpath(self.thirdAnswer)

    # click next
    def clickNext(self):
        self.base_page.clickElementByXpath(self.nextBtn)

    # get question content

    def getTextofQuestion(self):
        return self.base_page.getText(self.question)
    # get previous answers

    def getTextofPreviousAnswers(self):
        return self.base_page.getArrayText(self.previousAnswers)
