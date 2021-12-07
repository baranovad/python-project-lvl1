"""Try to figure out greatest common factor"""

import prompt
import random
import math


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print('Find the greatest common divisor of given numbers.')
    count_round = 3
    while count_round:
        number1 = random.randrange(1000)
        number2 = random.randrange(100)
        print('Question:{0}, {1}'.format(number1, number2))
        user_answer = prompt.string('Your answer:')
        gcd = math.gcd(number1, number2)
        if str(gcd) != user_answer:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {gcd}.)")
            print(f"Let's try again {name}")
            return
        else:
            print('Correct!')
        count_round -= 1
    print(f'Congratulations, {name}!')




