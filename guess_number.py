import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print('Welcome to the Gauss Number Guessing Game!')
    print('You will select a random number between 1 and 100. Now you can choose a number.')

    while not guessed:
        guess = int(input('Please enter your guess number: '))
        attempts += 1

        if guess < secret_number:
            print('Your guess number is low! Please try again!')
        elif guess > secret_number:
            print('Your guess number is high! Please try again!')
        else:
            guessed = True
            print(f'Congratulations, your guess number is {secret_number} in {attempts} attempts!')

    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again == 'y':
        guess_the_number()
    else:
        print('Thanks for playing. See you next time!')

# Main function call
guess_the_number()
