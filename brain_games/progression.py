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


def count_round():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, my name is {0}'.format(name))
    print("What number is missing in the progression?")
    round = 3
    while round:
        init_value = randint(1, 10)
        difference = randint(2, 10)
        hidden_index = randint(0, PROGRESSION_LENGTH - 1)
        correct_answer = init_value + difference * hidden_index
        string_result = make_progression(init_value, difference, hidden_index)
        print('Question:' + string_result)
        user_answer = prompt.string('Your answer:')
        if str(correct_answer) != user_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.)')
            print(f"Let's try again {name}")
            return
        else:
            print('Correct!')
        round -= 1
        print(f'Congratulations, {name}!')




