from radish import given, when, then
import pdb
import sys

@given("I have the numbers a = {a:g}, b = {b:g} and c = {c:g}")
def have_numbers(step, a, b, c):
    step.context.a = a
    step.context.b = b
    step.context.c = c

@when("I make them the coefficients of the biquadrate equation")
def sum_numbers(step):
    step.context.result = step.context.a + \
        step.context.b + step.context.c

@then("I expect it to have the following roots: {res:W}")
def expect_result(step, res):
    pdb.set_trace()
    with open("t.txt", "w") as f:
        print(3254, file=f)
    assert "7" == res