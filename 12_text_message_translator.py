# Many adults can’t understand text message abbreviations. Your challenge is to write a program
# that will take a text message and translate it into words your grandparents could understand.
# For example: So funny LOL ROTFL becomes So funny laughing out loud rolling on the floor laughing.
# For this scenario, we will start with a file that lists all the text message abbreviations and the translations.
# First, we have to break the problem into logical steps:
# 1. Have the user enter the text message.
# 2. Get a list of all the words in the text message.
# 3. Search the translation file for each word in the message and get the corresponding translation.
# 3a. Open the file which contains the translations.
# 3b. Extract all the abbreviations from the file and put them in a list.
# 3c. Extract all the translations from the file and put them in a list.
# 3d. For each word in the text message, go through the list of abbreviations looking for a match.
# 3e. When a match is found, display the corresponding translation.
# 4. Display the translation to the user.

all_abbreviations = []
all_translations = []
message = input('Please type below the text message you received:\n').upper().split()

with open('text_message_translator.txt', 'r') as file:
    content = file.readlines()
    for sentence in content:
        text = sentence.split()
        all_abbreviations.append(text[0])
        phrase = ' '.join(text[2:len(text)])
        all_translations.append(phrase)

for m in range(len(message)):
    for a in range(len(all_abbreviations)):
        if message[m] == all_abbreviations[a]:
            message[m] = all_translations[a]
        else:
            continue

print('\n\nYour text message means:\n%s' %' '.join(message).capitalize())