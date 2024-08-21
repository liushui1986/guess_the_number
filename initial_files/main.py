import random
from art import logo
target_num = random.randint(1, 100)


def game_difficulty(easiness):
    if easiness == 'easy':
        return 10
    elif easiness == 'hard':
        return 5
    else:
        print('Please choose "easy" or "hard": ')
        game_difficulty(easiness)


def game(attempt_times):
    while attempt_times >= 0:
        print(f'You have {attempt_times} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if guess == target_num:
            print(f'You got it! The answer was {guess}')
            break
        elif guess > target_num:
            attempt_times -= 1
            if attempt_times == 0:
                print('You used all attempts! Game Over!')
                break
            print('Too high.')
            print('Guess again.')
        else:
            attempt_times -= 1
            if attempt_times == 0:
                print('You used all attempts! Game Over!')
                break
            print('Too low.')
            print('Guess again.')


play = 'y'
while play == 'y':
    print('\n' * 100)
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    print('please guess the number that I\'m thinking')
    difficulty = input('You can choose a difficulty. Type \'easy\' or \'hard\': \n')
    game(game_difficulty(difficulty))
    play = input('Do you want to play "Guess The Number" game again? (Y/N)\n').lower()
