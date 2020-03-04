# Ask the user to enter the names of everyone invited for the party. Then return a list of the party guests in alphabetical order.
# This will require pulling together everything we have learned so far, so let’s walk through the thought process of idea to code.
# Put those values in a list. Sort the list. Print the sorted list.

guest_list = []
invitee = input('Who would you like to invite for the party? ').upper()

if invitee not in ('NONE', 'NO ONE'):
    while invitee not in ('NONE', 'NO ONE'):
        guest_list.append(invitee)
        guest_list.sort()
        invitee = input('Who else would you like to invite? ').upper()
    else:
        print('\n\nYou have invited:')
        for guest in guest_list:
            print(guest.capitalize())
else:
    print('\n\nYou have not invited anyone to the party.')
