from behave import given, when, then, step
from pages.checkoutCart import checkoutCart
from framework.webapp import webapp


@then(u'The Add to Cart Button exists on the page')
def step_impl(context):
    webapp.verify_component_exists_by_class_name("AddToCartButton-Desktop")

@when(u'I click add to cart')
def step_impl(context):
    checkoutCart.click_add_to_cart()

@when(u'I change the quanitity of books to "{newQuantity}"')
def step_impl(context, newQuantity):
    checkoutCart.change_quanitity(newQuantity)


@then(u'I the quanitity of books becomes "{quantity}"')
def step_impl(context, quantity):
    checkoutCart.verify_quantity(quantity)
    