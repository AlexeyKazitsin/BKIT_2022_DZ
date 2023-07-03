from behave import *
import sort


@given('the list is [3, -4, 4, 5, 0, 1, -1, 17]')
def step_impl(context):
    context.gdata = [3, -4, 4, 5, 0, 1, -1, 17]


@when('the list is sorted2')
def step_impl(context):
    context.gdata = sort.sort_1(context.gdata)


@then('the new list is [17, 5, -4, 4, 3, 1, -1, 0]')
def step_impl(context):
    assert context.gdata == [17, 5, -4, 4, 3, 1, -1, 0]
