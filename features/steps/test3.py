from behave import *
import sort


@given('the list is [0, -100, 100, 67, -67, 67, 99, 15, 16, -15]')
def step_impl(context):
    context.gdata = [0, -100, 100, 67, -67, 67, 99, 15, 16, -15]


@when('the list is sorted3')
def step_impl(context):
    context.gdata = sort.sort_1(context.gdata)


@then('the new list is [-100, 100, 99, 67, -67, 67, 16, 15, -15, 0]')
def step_impl(context):
    assert context.gdata == [-100, 100, 99, 67, -67, 67, 16, 15, -15, 0]
