#Help determine how much time someone has left to meet a deadline. Ask a user to enter the deadline for their project.
#Tell them how many days they have left to complete the project. For extra credit, give them the answer as a combination of weeks & days.
#(Hint: you will need some of the math functions from the module on numeric values)

import datetime

dueDate = input('When is the deadline for the project (mm/dd/yyyy)? ')
dueDate = datetime.datetime.strptime(dueDate, '%m/%d/%Y').date()
currentDate = datetime.date.today()
remainingWeeks = ((dueDate - currentDate) / 7).days
remainingDays = int((dueDate - currentDate).days) % 7

print('\n\n'f'There are only {remainingWeeks} week/s and {remainingDays} day/s left before the project is due')