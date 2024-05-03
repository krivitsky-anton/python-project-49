import prompt
import random


def create_progression() -> []:
    progression_length = random.randint(5, 10)
    progression_start = random.randint(1, 20)
    progression_step = random.randint(1, 9)
    progression_pointer = progression_start
    progression = []
    i = 0
    while i < progression_length:
        progression.append(progression_pointer)
        progression_pointer += progression_step
        i += 1
    return progression


wins = 0
print('Welcome to the Brain Games!')
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')
print('What number is missing in the progression?')

while wins < 3:
    new_progression = create_progression()
    position = random.randint(1, len(new_progression))
    correct_answer = new_progression[position]
    new_progression[position] = '..'
    print(f'Question: {new_progression}')
    user_answer = int(prompt.string('Your answer: '))
    if user_answer == correct_answer:
        print('Correct!')
        wins += 1
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        print(f'Let\'s try again, {user_name}!')
        break

if wins == 3:
    print(f'Congratulations, {user_name}!')