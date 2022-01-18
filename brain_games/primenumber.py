"""Find a prime number."""

import prompt
from random import randint


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor <= number // 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def find_primenumber():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    count_round = 3
    while count_round:
        number = randint(1, 100)
        print('Question:{0}'.format(number))
        user_answer = prompt.string('Your answer:')
        correct_answer = 'yes' if is_prime(number) else 'no'
        if correct_answer != user_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.)')
            print(f"Let's try again {name}")
            return
        else:
            print('Correct!')
        count_round -= 1
    print(f'Congratulations, {name}!')
