#! python3

#Mad Libs

import sys
import pyperclip

# Open text file to read and a new file to save new changed text.
text_file = open('textfile.txt', 'r+').read()
mltext = open('new_text.txt', 'r+')
print(text_file)
splitted_text = text_file.split()
print(splitted_text)

# TODO: Search for specific words while looping and replacing.
# them with user input.
for item in splitted_text:
    print(item)
    '''if x in ('ADJECTIVE'):
        print('Enter an adjective:')
        mltext.write(x.replace(x, input() + ''))
    elif x.startswith('NOUN'):
        print('Enter a noun:')
        mltext.write(x.replace(x, input() + ''))
    elif x.startswith('ADVERB'):
        print('Enter an adverb:')
        mltext.write(x.replace(x, input() + ''))
    elif x.startswith('VERB'):
        print('Enter a verb:')
        mltext.write(x.replace(x, input() + ''))
    else:
        mltext.write(x + ' ')

    '''
    
mltext.close()
mltext = open('new_text.txt').read()
print(mltext)
    


# TODO: Print new text and save it to a new file.


# TODO: Change project status to "finished".
