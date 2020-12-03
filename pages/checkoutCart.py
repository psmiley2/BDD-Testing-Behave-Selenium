from framework.webapp import webapp
from selenium.webdriver.support.ui import Select

class CheckoutCart():
    instance = None
    

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CheckoutCart()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.addToCartClassName = "AddToCartButton-Desktop"
        self.quantityClassName = "DropdownInput"

    def click_add_to_cart(self):
        webapp.click_button_with_class_name(addToCartClassName)

    def change_quanitity(self, newQuantity):
        dropDown = Select(self.driver.find_element_by_class_name(self.quantityClassName))
        dropDown.select_by_value(newQuantity)

    def verify_quantity(self, quantity):
        recievedQuantity = self.driver.find_element_by_class_name(self.quantityClassName)
        assert recievedQuantity == quantity

checkoutCart = CheckoutCart.get_instance()