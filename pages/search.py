from framework.webapp import webapp
from selenium.webdriver.common.keys import Keys

class Search():
    instance = None
    

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Search()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.searchBoxClassName = "Search-input"

    def verify_typing_in_search_box(self, text):
        searchBox = self.driver.find_element_by_class_name(self.searchBoxClassName)
        searchBox.send_keys(text)

    def verify_search_box_contains_text(self, text):
        searchBox = self.driver.find_element_by_class_name(self.searchBoxClassName)
        assert searchBox.get_attribute("value") == text

    def search_for_text(self, text):
        searchBox = self.driver.find_element_by_class_name(self.searchBoxClassName)
        searchBox.send_keys(text)
        search.send_keys(Keys.RETURN)

search = Search.get_instance()