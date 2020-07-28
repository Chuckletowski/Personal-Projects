# Write a program that will draw a pyramid figure on the screen. Ask the user how tall they want their pyramid to be.
# For extra credit, let them choose what character on the keyboard they want to use for their drawing.

character = input('What character do you want to use for drawing? ')
row = int(input('How many rows do you want your pyramid to have? '))
space = row - 1
draw = 1

print('\n\n')

for r in range(row):
    for s in range(space):
        print(' ', end = '')
    space -= 1
    for d in range(draw):
        print(character, end = '')
    draw += 2
    print()
