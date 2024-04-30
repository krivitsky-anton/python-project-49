import prompt
import random


def get_random_number() -> int:
    return random.randint(1, 100)


def is_even(num: int):
    if num % 2 == 0:
        return 'yes'
    return 'no'


wins = 0
print('Welcome to the Brain Games!')
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
while wins < 3:
    number = get_random_number()
    correct_answer = is_even(number)
    user_answer = prompt.string(f'Question: {number} ')
    if user_answer == correct_answer:
        print('Correct!')
        wins += 1
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        print(f'Let\'s try again, {user_name}!')
        break

if wins == 3:
    print(f'Congratulations, {user_name}!')
