import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print('Welcome to the gauss number game!')
    print('You will select a random number between 1 and 100. Now you can choose a random number')
    while not guessed:
        guess = int(input('Please enter your guess number: '))
        attempts += 1
        if guess < secret_number:
            print('Your guess number is low! Please try again!')
        elif guess > secret_number:
            print('Your guess number is high! Please try again!')
        else:
            guessed = True
            print(f'Congrasulation, Your guess number is {secret_number} in {attempts} attempts times.')
        
    play_again = input('Do you want to play again! (y/n):')
    if play_again == 'y':
        guess_the_number()
    else:
        print('Thanks for playing')


# main funciton call 
guess_the_number()