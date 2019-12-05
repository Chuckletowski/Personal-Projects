# Help determine how much time someone has left to meet a deadline. Ask a user to enter the deadline for their project.
# Tell them how many days they have left to complete the project. For extra credit, give them the answer as a combination
# of weeks & days. (Hint: You will need some of the math functions from the module on numeric values).

import datetime

due_date = input('When is the deadline for the project (mm/dd/yyyy)? ')
due_date = datetime.datetime.strptime(due_date, '%m/%d/%Y').date()
current_date = datetime.date.today()
remaining_weeks = ((due_date - current_date) / 7).days
remaining_days = int((due_date - current_date).days) % 7

print(f'\n\nThere are only {remaining_weeks} week/s and {remaining_days} day/s left before the project is due')
