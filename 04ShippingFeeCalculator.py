#Calculate shipping charges for a shopper. Ask the user to enter the amount for their total purchase.
#If their total is under $50, add $10. Otherwise, shipping is free.
#Tell the user their final total including shipping costs and format the number so it looks like a monetary value.
#Don’t forget to test your solution with:
#A value > 50
#A value < 50
#A value of exactly 50

limitAmount = 50
shippingFee = 10

totalAmount = float(input('How much is your total shopping cost? $'))

if totalAmount < limitAmount:
    totalAmount += shippingFee
    print('\n\nYour overall charge is $%.2f, an additional $%d has been charged for shipping fee' %(totalAmount, shippingFee))
else:
    print('\n\nYour overall charge is $%.2f with free shipping' %totalAmount)
