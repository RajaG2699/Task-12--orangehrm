from data import data
from selenium.webdriver.common.by import By

from Locators import Locators


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException





class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)


   def quit(self):
       self.driver.quit()


   def login(self):
       try:
           self.boot()


           # Username - 4
           # Password - 5
           # Test Results - 6


           for row in range(2, data.WebData().rowCount()+1):
               username = data.WebData().readData(row, 6)
               password = data.WebData().readData(row, 7)
               print(username,password)

               Locators.WebLocators().enterText(self.driver, Locators.WebLocators().usernameLocator, username)
               Locators.WebLocators().enterText(self.driver, Locators.WebLocators().passwordLocator, password)
               Locators.WebLocators().clickButton(self.driver, Locators.WebLocators().buttonLocator)
               self.driver.implicitly_wait(10)
               if self.driver.current_url == data.WebData().dashboardURL:
                   print("Successfully LoggedIn")
                   data.WebData().writeData(row, 8, "PASSED")
               else:
                   print("Login Unsuccessful")
                   data.WebData().writeData(row, 8, "FAILED")


       except NoSuchElementException as e:
           print("Error!")
       finally:
           self.quit()


obj = LoginPage()
obj.login()
