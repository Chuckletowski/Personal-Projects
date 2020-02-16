#Write a program that generates a random number between 0-9 and asks you to guess it. You only have three attempts
#to guess the hidden number. Use a while loop to let the user keep guessing so long as the number of guesses left
#is greater than zero. Ask the user for their guess number. If they guess it correctly, print 'You win' and break.
#If not, decrement the number of guesses left by one until there are no more attempts left and print 'You lose'.

from random import randint

mystery_number = randint(0,9)
guess_number = int(input('Guess the mystery number (0-9 only): '))
number_of_guess = 3
remaining_guess = number_of_guess - 1

while number_of_guess > 0:
    if mystery_number != guess_number:
        if remaining_guess > 0:
            print(f'Wrong guess. {guess_number} is not the mystery number. You only have {remaining_guess} guess/es left.')
            guess_number = int(input('Guess the mystery number (0-9 only): '))
            remaining_guess -= 1
            number_of_guess -= 1
        else:
            print(f'\n\nSorry, you lose. The mystery number is {mystery_number}.')
            break
    else:
        print(f'\n\nCongratulations, you win. The mystery number is {mystery_number}.')
        break