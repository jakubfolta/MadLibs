#! python3

#Mad Libs

import sys
import pyperclip

# Open text file to read and a new file to save new changed text.
text_file = open('textfile.txt')
mltext = open('new_text.txt', 'w')
file_content = text_file.read()
# Split text file.
splitted_text = file_content.split()
print(file_content)
print(splitted_text)

# TODO: Search for specific words while looping and replacing.
# them with user input.
for x in splitted_text:
    if x == splitted_text[len(splitted_text) - 1] and x not in ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']:
        mltext.write(x)
    elif x == 'ADJECTIVE':
        if x == splitted_text[len(splitted_text) - 1]:
            print('Enter an adjective:')
            mltext.write(x.replace(x, input()))
        else:
            print('Enter an adjective:')
            mltext.write(x.replace(x, input() + ' '))
            print(x)
    else:
        mltext.write(x + ' ')
mltext.close()
mltext = open('new_text.txt')
print(mltext.read())
    
    

# TODO: Print new text and save it to a new file.


# TODO: Change project status to "finished".
