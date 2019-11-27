#Calculate the total to charge for an order from an online store in Canada. Ask user what country they are from and their order total.
#If the user is from Canada, ask which province. If the order is from outside Canada, do not charge any taxes.
#If the order was placed in Canada, calculate tax based on the province. Alberta charges .05% General Sales Tax.
#Ontario, New Brunswick, and Nova Scotia charge .13% Harmonized Sales Tax. All other provinces charge .06% Provincial Sales Tax +
#.05% General Sales Tax. Tell the user the total with taxes for their order.

gst = .0005
hst = .0013
pst = .0006

totalAmount = float(input('How much is your total order cost? $'))
country = input('What country are you from? ').upper()

if country == 'CANADA':
    province = input('Which province are you from? ').upper()
    if province == 'ALBERTA':
        totalAmount = (totalAmount * gst) + totalAmount
    elif province == 'ONTARIO' or province == 'NEW BRUNSWICK' or province == 'NOVA SCOTIA':
        totalAmount = (totalAmount * hst) + totalAmount
    else:
        totalAmount = ((totalAmount * pst) + (totalAmount * gst)) + totalAmount
    print('\n\nYour overall charge is $%.2f' %totalAmount)
else:
    print('\n\nYour overall charge is $%.2f' %totalAmount)
