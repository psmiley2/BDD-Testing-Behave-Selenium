from framework.webapp import webapp
from selenium.webdriver.common.keys import Keys

class Review():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Review()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.headlineClassName = "WorkReview-textInput"
        self.reviewClassName = "WorkReview-textArea"
        self.displayNameClassName = "WorkReview-displayTextInput"

    def type_in_headline(self, headline):
        headlineField = self.driver.find_element_by_class_name(self.headlineClassName)
        headlineField.send_keys(headline)

    def verify_headline(self, headline):
        headlineField = self.driver.find_element_by_class_name(self.headlineClassName)
        assert headlineField.get_attribute("value") == headline

    def verify_star_count(self, s):
        stars = self.driver.find_element_by_class_name("WorkReviews-rating")
        assert stars == s

  
    def type_in_review(self, review):
        reviewField = self.driver.find_element_by_class_name(self.reviewClassName)
        reviewField.send_keys(review)


    def verify_review(self, review):
        reviewField = self.driver.find_element_by_class_name(self.reviewClassName)
        assert reviewField.get_attribute("value") == review

    def type_in_display_name(self, displayName):
        displayNameField = self.driver.find_element_by_class_name(self.displayNameClassName)
        displayNameField.send_keys(displayName)

    def verify_display_name(self, displayName):
        displayNameField = self.driver.find_element_by_class_name(self.displayNameClassName)
        assert displayNameField.get_attribute("value") == displayName

review = Review.get_instance()