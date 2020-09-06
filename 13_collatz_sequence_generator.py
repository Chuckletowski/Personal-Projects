#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1

digit = input('Please give a positive whole number: ')

try:
    if int(digit) > 0:
        print('\n\nThe Collatz sequence is:\n%d' %int(digit))
        while digit != 1:
            digit = collatz(int(digit))
            print(int(digit))
    elif int(digit) <= 0:
        print('\n\nSorry, only positive whole numbers are accepted.')
except ValueError:
    print('\n\nSorry, only positive whole numbers are accepted.')