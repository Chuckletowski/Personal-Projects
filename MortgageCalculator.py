loanAmount = float(input('What is your desired loan amount? $'))
interestRate = float(input('What is the current annual interest rate? %')) * .01 / 12
numberYears = float(input('How many years do you plan to pay the loan? ')) * 12
monthlyPayment = (loanAmount * (interestRate * (1 + interestRate) * numberYears)) / ((1 + interestRate) * numberYears - 1)

print('\n\n''Your monthly payment would be: $%.2f' %monthlyPayment)