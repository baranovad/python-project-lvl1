"""Find a prime number."""

import prompt
from random import randint


def is_prime(question):
    """is_prime(question) helps to find the prime numbers."""
    if question < 2:
        return False
    divisor = 2
    while divisor <= question // 2:
        if question % divisor == 0:
            return False
        divisor += 1
    return True


def generate_data():
    """generate_data() helps to generate the game."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
