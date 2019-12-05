# Have the user enter the cost of the loan, the interest rate, and the number of years for the loan and calculate monthly payments
# with the following formula: M = L[i(1+i)n] / [(1+i)n-1]
# Where:
# M = monthly payment
# L = Loan amount 
# i = interest rate (for an interest rate of 5%, i = 0.05)
# n = number of payments

loanAmount = float(input('What is your desired loan amount? $'))
interestRate = float(input('What is the current annual interest rate? %')) * .01 / 12
numberYears = float(input('How many years do you plan to pay the loan? ')) * 12
monthlyPayment = (loanAmount * (interestRate * (1 + interestRate) * numberYears)) / ((1 + interestRate) * numberYears - 1)

print('\n\nYour monthly payment would be: $%.2f' %monthlyPayment)
