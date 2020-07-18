# Write a program that will create a CSV file for incoming college students. Ask the user to enter the student information needed
# for the records. Then open the CSV file and print all the entries in the student record. For extra credit, you may use a
# special function to display the printed list neatly and presentably.

from csv import reader

student_number = input('Please provide student number: ')
full_name = input('Please provide full name: ').upper()
birthdate = input('Please provide birthdate (mm/dd/yyyy): ')
gender = input('Please provide gender (M/F): ').upper()
home_address = input('Please provide home address: ').upper()
mobile_number = input('Please provide mobile number: ')
email_address = input('Please provide email address: ').lower()
course = input('Please provide course: ').upper()

with open('college_admission_list.csv', 'a') as record_file:
    record_file.write(f'{student_number}|{full_name}|{birthdate}|{gender}|{home_address}|{mobile_number}|{email_address}|{course}\n')

print('\n\nFile updated successfully.\n\n')

with open('college_admission_list.csv', 'r') as record_file:
    record_list = reader(record_file, delimiter = '|')
    for record in record_list:
        print(', '.join(record))
