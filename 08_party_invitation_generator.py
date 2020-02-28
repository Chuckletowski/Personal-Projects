#Ask the user to enter the names of everyone attending a party
#Then return a list of the party guests in alphabetical order
#This will require pulling together everything we have learned so far, so let’s walk through the thought process of idea to code
#Put those values in a list
#Sort the list
#Print the sorted list

from sys import exit
guest_list = []
invitee = input('Who would you like to invite for the party? ').upper

if invitee != 'NONE':
    while invitee != 'NONE':
        guest_list.append(invitee)
        invitee = input('Who else would you like to invite? ').upper
    else:
        guest_list.sort
        print('\n\nYou have invited:')
        for guest in guest_list:
            print(guest).capitalize
else:
    exit()