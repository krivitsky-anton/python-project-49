import prompt
import random


def is_prime(num: int):
    i = 2
    while i < num:
        if num % i == 0:
            return 'no'
        i += 1
    return 'yes'


wins = 0
print('Welcome to the Brain Games!')
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
while wins < 3:
    number = random.randint(1, 1000)
    correct_answer = is_prime(number)
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
