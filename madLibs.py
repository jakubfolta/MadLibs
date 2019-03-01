#! python3

#Mad Libs

import sys
import pyperclip

# Open text file to read and a new file to save new changed text.
text_file = open('textfile.txt').read()
mltext = open('new_text.txt', 'r+')
file_content = text_file
print(text_file)

# Split text file.
splitted_text = file_content.split()
print(file_content)
print(splitted_text)


# TODO: Search for specific words while looping and replacing.
# them with user input.
for x in file_content:
    if x.startswith('ADJECTIVE'):
        print('Enter an adjective:')
        mltext.write(x.replace(x, input() + ' '))
    elif x.startswith('NOUN'):
        print('Enter a noun:')
        mltext.write(x.replace(x, input() + ' '))
    elif x.startswith('ADVERB'):
        print('Enter an adverb:')
        mltext.write(x.replace(x, input() + ' '))
    elif x.startswith('VERB'):
        print('Enter a verb:')
        mltext.write(x.replace(x, input() + ' '))
    else:
        mltext.write(x + ' ')

    
    
mltext.close()
mltext = open('new_text.txt')
print(mltext.read())
    


# TODO: Print new text and save it to a new file.


# TODO: Change project status to "finished".
