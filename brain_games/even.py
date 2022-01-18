"""Try to figure out if number is odd or even."""

import prompt
import random


def is_even(number):
    return number % 2 == 0


def brain_games_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_round = 3
    while count_round:
        number = random.randrange(100)
        print('Question:{0}'.format(number))
        user_answer = prompt.string('Your answer:')
        correct_answer = 'yes' if is_even(number) else 'no'
        if correct_answer != user_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.)')
            print(f"Let's try again {name}")
            return
        count_round -= 1
    print(f'Congratulations, {name}!')
