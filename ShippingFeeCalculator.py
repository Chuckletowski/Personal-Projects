#Calculate shipping charges for a shopper. Ask the user to enter the amount for their total purchase.
#If their total is under $50, add $10. Otherwise, shipping is free.
#Tell the user their final total including shipping costs and format
#the number so it looks like a monetary value.
#•	Don’t forget to test your solution with 
#–	a value > 50
#–	a value < 50
#–	a value of exactly 50

totalAmount = float(input('How much is your total shopping cost? $'))

if totalAmount < 50:
    totalAmount += 10
    print('\n\nYour overall charge is $%.2f, an additional $10 has been charged for shipping fee' %totalAmount)
else:
    print('\n\nYour overall charge is $%.2f with free shipping' %totalAmount)