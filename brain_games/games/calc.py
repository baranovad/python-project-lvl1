"""Make a calculator."""
from random import randint, choice

def calculate(number1, number2, operator):
    result_calc = 0
    if operator == '+':
        result_calc = number1 + number2
    elif operator == '-':
        result_calc = number1 - number2
    elif operator == '*':
        result_calc = number1 * number2
    return result_calc


def generate_data():
    number1 = randint(1, 10)
    number2 = randint(1, 10)

    operator = ['+', '-', '*']
    picked_operator = choice(operator)
    question = '{} {} {}'.format(number1, picked_operator, number2)
    correct_answer = calculate(number1, number2, picked_operator)

    return question, str(correct_answer)

