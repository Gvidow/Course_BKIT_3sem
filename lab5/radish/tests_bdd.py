from radish import given, when, then, custom_type, register_custom_type, TypeBuilder
import sys
import os

sys.path.append(os.getcwd())
import BiSquareRoot


@custom_type('Number', r"\d*")
def parse_number(text):
    res = None
    try:
        res = int(text)
    except Exception:
        pass
    return res

register_custom_type(NumberList=TypeBuilder.with_many(
    parse_number, listsep=','))

@given('I have the numbers {numbers:NumberList}')
def have_numbers(step, numbers):
    step.context.factors = list(filter(lambda x: isinstance(x, (int, float)), numbers))


@when("I make them the coefficients of the biquadrate equation")
def sum_numbers(step):
    if len(step.context.factors) != 3:
        step.context.result = [None]
        return
    equation = BiSquareRoot.BiSquareRoot(*step.context.factors)
    step.context.result = equation.calculate()
    if len(step.context.result) == 0:
        step.context.result = [None]

@then("I expect it to have the following roots: {res:NumberList}")
def expect_result(step, res):
    print(res)
    assert step.context.result == res
