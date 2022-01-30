"""Find a progression."""

from random import randint
import prompt

PROGRESSION_LENGTH = 10


def make_progression(init_value, difference, hidden_index):
    counter = 0
    string_result = ''
    while counter < PROGRESSION_LENGTH:
        current_value = init_value + counter * difference
        if hidden_index == counter:
            string_result += ' ..'
        else:
            string_result += ' ' + str(current_value)
        counter += 1
    return string_result


def generate_data():
    init_value = randint(1, 10)
    difference = randint(2, 10)
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = init_value + difference * hidden_index
    question = make_progression(init_value, difference, hidden_index)
    return question, str(correct_answer)