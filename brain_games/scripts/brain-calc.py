import prompt
import random


def add(num1: int, num2: int):
    return num1 + num2


def sub(num1: int, num2: int):
    return num1 - num2


def mult(num1: int, num2: int):
    return num1 * num2


def game_round():
    number1 = random.randint(1, 25)
    number2 = random.randint(1, 25)
    operation = random.randint(1, 3)
    if operation == 1:
        correct_answer = add(number1, number2)
        user_answer = int(prompt.string(f'Question: {number1} + {number2} '))
        if user_answer == correct_answer:
            return True
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        return False
    elif operation == 2:
        correct_answer = sub(number1, number2)
        user_answer = int(prompt.string(f'Question: {number1} - {number2} '))
        if user_answer == correct_answer:
            return True
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        return False
    else:
        correct_answer = mult(number1, number2)
        user_answer = int(prompt.string(f'Question: {number1} * {number2} '))
        if user_answer == correct_answer:
            return True
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer is \'{correct_answer}\'')
        return False


wins = 0
print('Welcome to the Brain Games!')
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

print('What is the result of the expression?')
while wins < 3:
    if game_round():
        print('Correct!')
        wins += 1
    else:
        print(f'Let\'s try again, {user_name}!')
        break

if wins == 3:
    print(f'Congratulations, {user_name}!')



