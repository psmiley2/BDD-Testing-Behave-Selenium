from behave import given, when, then, step
from pages.review import review
from framework.webapp import webapp

@then(u'I click Write a Review')
def step_impl(context):
    webapp.click_button_with_class_name("WorkReviews-writeButton")

@when(u'I type "{headline}" in the headline')
def step_impl(context, headline):
    review.type_in_headline(headline)


@then(u'The text "{headline}" is in the headline')
def step_impl(context, headline):
    review.verify_headline(headline)

@when(u'I click "{s}" star(s)')
def step_impl(context, s):
    webapp.click_button_with_class_name("WorkReviews-rating-5star-btn")

@then(u'The review has "{s}" star(s)')
def step_impl(context, s):
    review.verify_star_count(s)

@when(u'I type "{review}" in the review')
def step_impl(context, review):
    review.type_in_review(review)


@then(u'The text "{review}" is in the review')
def step_impl(context, review):
    review.verify_review(review)


@when(u'I type "{displayName}" in the display name')
def step_impl(context, displayName):
    review.type_in_display_name(displayName)


@then(u'The text "{displayName}" is in the display name')
def step_impl(context, displayName):
    review.verify_display_name(displayName)