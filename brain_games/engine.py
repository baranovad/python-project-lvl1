"""core for the games"""

import prompt

ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')

    count = ROUNDS_COUNT
    while count:
        question, correct_answer = game.generate_data()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.)')
            print(f"Let's try again {name}")
            return

        print('Correct!')
        count -= 1

    print(f'Congratulations, {name}!')
