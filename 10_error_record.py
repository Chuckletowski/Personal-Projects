# Create a function with two parameters. One parameter to hold a string of text. One parameter to hold a filename.
# Write a code in the function that will write the text to a file with the name specified.

from datetime import datetime

def write_error(error_code, filename):
    with open(filename, 'a') as file:
        report_date = datetime.now().strftime('%d-%b-%Y %H:%M:%S')
        file.write(f'{error_code}{error_message}|{report_date}\n')

error_code = input('What is the error code you encountered? ')
filename = 'error_record.csv'

if error_code == '101':
    error_message = ': Uncommitted Transaction Batch'
elif error_code == '102':
    error_message = ': Invalid Import Control'
elif error_code == '103':
    error_message = ': Unknown Connector Type'
elif error_code == '104':
    error_message = ': Option Schema Conflict'
else:
    error_message = ': Record update needed due to new error code encountered'

write_error(error_code, filename)

print('\n\nError logged to the file.')
