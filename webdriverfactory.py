from selenium import webdriver
import os

class WebdriverFactory():
    def __init__(self,browser):
        self.driver_location_chrome = "C:\\Users\\jnav\\PycharmProjects\\Myntraonlineshopping\\driverexecutables\\chromedriver.exe"
        self.driver_location_firefox = "driverexecutables\\geckodriver.exe"
        self.driver_location_ie = "driverexecutables\\IEDriverServer.exe"
        os.environ["webdriver.chrome.driver"] = self.driver_location_chrome
        os.environ["webdriver.gecko.driver"] = self.driver_location_firefox
        os.environ["webdriver.ie.driver"] = self.driver_location_ie
        self.browser = browser


    def getWebDriverInstance(self):

        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.driver_location_chrome)
            print("Execution starts on chrome browser")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=self.driver_location_firefox)
            print("Execution starts on ff browser")
        else:
            driver = webdriver.Ie(executable_path=self.driver_location_ie)
            print("Execution starts on ie browser")
        driver.get("https://www.myntra.com/login?referer=https://www.myntra.com/?gclid=Cj0KCQjw6KrtBRDLARIsAKzvQIERdtbTGqPnZ5raELDeG7XfCDI6BBM06L6pzgCpE85k2GTv_liIwqMaAoXjEALw_wcB")
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver


