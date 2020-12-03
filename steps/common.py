from behave import given, when, then, step
from framework.webapp import webapp

@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()

@then(u'I close the website')
def step_impl_close_website(context):
    webapp.close_website()

@given(u'I return to the homepage')
def step_impl_goto_homepage(context):
    webapp.goto_page("https://www.thriftbooks.com/")

@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    webapp.goto_page(page)

@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)

@then(u'I do not see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_does_not_exist(component)

@then(u'I see a component with className "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists_by_class_name(component)