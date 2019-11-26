#Calculate the total to charge for an order from an online store in Canada.
#Ask user what country they are from and their order total
#•	If the user is from Canada, ask which province
#•	If the order is from outside Canada do not charge any taxes
#•	If the order was placed in Canada calculate tax based on the province
#–	Alberta charge .05% General sales Tax (GST)
#–	Ontario, New Brunswick, Nova Scotia charge .13% Harmonized sales tax
#–	All other provinces charge .06% provincial sales tax + .05% GST tax
#•	Tell the user the total with taxes for their order

totalAmount = float(input('How much is your total order cost? $'))
country = input('What country are you from? ').upper()

if country == 'CANADA':
    province = input('Which province are you from? ').upper()
    if province == 'ALBERTA':
        totalAmount = (totalAmount * .0005) + totalAmount
    elif province == 'ONTARIO' or province == 'NEW BRUNSWICK' or province == 'NOVA SCOTIA':
        totalAmount = (totalAmount * .0013) + totalAmount
    else:
        totalAmount = ((totalAmount * .0006) + (totalAmount * .0005)) + totalAmount
    print('\n\nYour overall charge is $%.2f' %totalAmount)
else:
    print('\n\nYour overall charge is $%.2f' %totalAmount)