# SUPER IMPORTANT: In order for this to work, the person running this code must 
# have a chromedriver matching their current chrome version in their
# Program Files (x86) folder

from selenium import webdriver
from urllib.parse import urljoin


class WebApp:
    instance = None
    url = "https://www.thriftbooks.com/"

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        # self.driver = webdriver.Firefox()
        PATH = "C:\Program Files (x86)\chromedriver.exe" 
        self.driver = webdriver.Chrome(PATH)

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(self.url)

    def close_website(self):
        self.driver.quit()

    def goto_page(self, page):
        self.driver.get(urljoin(self.url, page.lower()))

    def verify_component_exists(self, component):
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)

    def verify_component_does_not_exis(self, component):
            assert component not in self.driver.find_element_by_tag_name('body').text
            
    def verify_component_exists_by_class_name(self, className):
        assert self.driver.find_element_by_class_name(className) is not None

    def click_button_with_class_name(self, className):
        button = self.driver.find_element_by_class_name(className)
        assert button is not None
        button.click()

webapp = WebApp.get_instance()