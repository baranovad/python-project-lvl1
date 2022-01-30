"""Try to figure out the greatest common factor."""

from random import randint, choice
import math


def generate_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{} {}'.format(number1, number2)
    correct_answer = math.gcd(number1, number2)
    return question, str(correct_answer)
