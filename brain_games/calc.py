"""Make a calculator"""


import prompt
import random


def calculate(number1, number2, operator):
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    return result


def brain_games_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print('What is the result of the expression?')
    count_round = 3
    while count_round:
        number1 = random.randrange(10)
        number2 = random.randrange(10)
        operator = ['+', '-', '*']
        picked_operator = random.choice(operator)
        expression = '{} {} {}'.format(number1, picked_operator, number2)
        print('Question:{0}'.format(expression))
        user_answer = prompt.string('Your answer:')
        correct_answer = str(calculate(number1, number2, picked_operator))
        if correct_answer != user_answer:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.)")
            print(f"Let's try again {name}")
            return
        else:
            print('Correct!')
        count_round -= 1
    print(f'Congratulations, {name}!')





