import prompt
import random
import math


def get_gcd(num1: int, num2: int):
    return (num1 * num2) // math.gcd(num1, num2)


wins = 0
print('Welcome to the Brain Games!')
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

print('Find the greatest common divisor of given numbers.')
while wins < 3:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    correct_answer = get_gcd(number1, number2)
    user_answer = int(prompt.string(f'Question: {number1} {number2} '))
    if user_answer == correct_answer:
        print('Correct!')
        wins += 1
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        print(f'Let\'s try again, {user_name}!')
        break

if wins == 3:
    print(f'Congratulations, {user_name}!')
