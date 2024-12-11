import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from PageObjects.LanguagePage import Page
class ArticlesCount :

    def __init__(self,languages,driver):
        self.driver=driver
        val2="jhf"
        val1="jdfhvj"
        val="khfvb"
        self.languages = languages

    def findTotalArticlesByLanguages(self):

        #Creating object Languagepage function

        Languagepage_obj = Page(driver)
        Languagepage_obj.launch_chrome()
        final_count = Languagepage_obj.articles_count(self.languages)
        return final_count

# Chrome Browser Launching

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

# Passing the Languages in list
languages = ["English","German"]

#Creating Object for test action class
object = Logic(languages,driver)
final_count = object.findTotalArticlesByLanguages()
print(final_count)
test='jhfv'