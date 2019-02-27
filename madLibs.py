#! python3

#Mad Libs

import sys
import pyperclip
import shelve

# Open text file to read and a new file to save new changed text.
text_file = open('textfile.txt')
mltext = open('new_text.txt', 'w')
file_content = text_file.read()
# Split text file.
splitted_text = file_content.split()
print(file_content)
print(splitted_text)

# TODO: Search for specific words while looping and replacing.
#   them with user input.
for x in splitted_text :
    if x == 'ADJECTIVE':
        print('Enter an adjective:')
        input
        
    

# TODO: Print new text and save it to a new file.


# TODO: Change project status to "finished".
