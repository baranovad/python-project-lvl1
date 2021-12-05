"""brain games."""

import prompt


def welcome_user():
    """welcome_user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
