from selenium.webdriver.common.by import By


class GenericMethods :
    def __init__(self,driver):
        self.driver = driver

    def launch_url(self):
        self.driver.get("https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table")

    def return_text(self,Articlecount):
        value = self.driver.find_element(By.XPATH ,Articlecount ).text
        return value



