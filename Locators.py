from selenium.webdriver.common.by import By




class WebLocators:


   def __init__(self):
       self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
       self.passwordLocator = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
       self.buttonLocator = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"




   def enterText(self, driver, locator, textValue):
       element = driver.find_element(by=By.XPATH, value=locator)
       element.clear()
       element.send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()
