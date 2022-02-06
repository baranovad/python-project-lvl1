"""Try to figure out if number is odd or even."""

import random


def is_even(question):
    """is_even(question) helps to find the even number."""
    return question % 2 == 0


def generate_data():
    """generate_data() helps to generate the game."""
    question = random.randrange(100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
