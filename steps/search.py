from behave import given, when, then, step
from pages.search import search
from framework.webapp import webapp

@when(u'I type "{text}" in the the search box')
def step_impl_type_in_search_box(context, text):
    search.verify_typing_in_search_box(text)


@when(u'I search for "{text}"')
def step_impl_search_for_text(context, text):
    search.search_for_text(text)

@when(u'I clear the text field')
def step_impl(context):
    webapp.click_button_with_class_name("Search-rest")

@then(u'The title "{title}" by "{author}" appears as the first result')
def step_impl(context, title, author):
    webapp.verify_component_exists(title)
    webapp.verify_component_exists(author)

@then(u'The title "{title}" by "{author}" appears')
def step_impl(context, title, author):
    webapp.verify_component_exists(title)
    webapp.verify_component_exists(author)

@then(u'The search box is empty')
def step_impl(context):
    search.verify_search_box_contains_text("")

@then(u'The text "We couldn\'t find a match" appears')
def step_impl(context):
    webapp.verify_component_exists(u'The text "We couldn\'t find a match" appears')

@then(u'The text "{text}" appears in the search box')
def step_impl_check_text_in_search_box(context, text):
    search.verify_search_box_contains_text(text)