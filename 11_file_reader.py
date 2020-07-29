# Write a code that will open and read a file. Allow the user to specify the filename to be accessed.
# Add an error handling procedure to provide a suitable error message in a scenario where the file specified by the user could not be found.

from csv import reader

print('Please give the CSV file you want to open in this format - \'filename.extension\'')
filename = input('Type it here: ').lower()
print('\n')

try:
    with open(filename, 'r') as file:
        content = reader(file, delimiter = '|')
        for item in content:
            print(': '.join(item))
except FileNotFoundError:
    print(f'File \'{filename}\' not found. Kindly check the filename and/or extension and try again.')