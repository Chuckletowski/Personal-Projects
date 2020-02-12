#Write a program that generates a random number (0-9) and ask you to guess it. You have three asserts.
#Define a random_number with randit between 0-9.
#Initialize guesses_left to 3.
#Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
#Ask the user for their guess, just like the second example above.
#If they guess correctly, print 'You win!' and break. Decrement guesses_left by one.
#Use an else: case after your while loop to print:You lose.

from random import randint

random_number = randint(0,9)
guess_number = int(input('Guess the hidden number: '))
number_of_guess = 3
remaining_guess = number_of_guess - 1

while number_of_guess > 0:
    if random_number != guess_number:
        print(f'\n\nWrong guess. {guess_number} is not the hidden number. You only have {remaining_guess} guess/es left.')
        guess_number = int(input('Guess the hidden number: '))
        number_of_guess -= 1
        remaining_guess -= 1
    else:
        print(f'Congratulations, you win. The hidden number is {random_number}.')
        break
else:
    print(f'Sorry, you lose. The hidden number is {random_number}.')