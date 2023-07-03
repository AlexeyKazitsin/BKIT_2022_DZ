from behave import *
import sort


@given('the list is [3, -4, 5, 0, 1]')
def step_impl(context):
    context.gdata = [3, -4, 5, 0, 1]


@when('the list is sorted')
def step_impl(context):
    context.gdata = sort.sort_1(context.gdata)


@then('the new list is [5, -4, 3, 1, 0]')
def step_impl(context):
    assert context.gdata == [5, -4, 3, 1, 0]
