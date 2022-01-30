"""Try to figure out if number is odd or even."""

import random


def is_even(question):
    return question % 2 == 0


def generate_data():
    question = random.randrange(100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
