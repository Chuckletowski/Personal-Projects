# Calculate shipping charges for a shopper. Ask the user to enter the amount for their total purchase.
# If their total is under $50, add $10. Otherwise, shipping is free.
# Tell the user their final total including shipping costs and format the number so it looks like a monetary value.
# Don’t forget to test your solution with:
# A value > 50
# A value < 50
# A value of exactly 50

limit_amount = 50
shipping_fee = 10
total_amount = float(input('How much is your total shopping cost? $'))

if total_amount < limit_amount:
    total_amount += shipping_fee
    print('\n\nYour overall charge is $%.2f, an additional $%d has been charged for shipping fee' %(total_amount, shipping_fee))
else:
    print('\n\nYour overall charge is $%.2f with free shipping' %total_amount)
