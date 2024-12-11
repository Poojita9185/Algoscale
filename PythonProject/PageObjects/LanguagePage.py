from PageObjects.Genericfunctions import GenericMethods


class Page(GenericMethods) :
    def __init__(self,driver):
        super().__init__(driver)

    Article_count = "//a[text()='?']/parent :: td/following-sibling :: td[3]/a"

   #Launching URL

    def launch_chrome(self):
        self.driver.maximize_window()
        self.launch_url()

    # Sum of articles count

    def articles_count(self,languages):
        count =0
        for i in languages :
            text_val = self.return_text(self.Article_count.replace('?',i))
            text_val=text_val.replace(",","")
            count=count + int(text_val)

        return count




