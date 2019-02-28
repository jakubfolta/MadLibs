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
for index, x in enumerate(splitted_text):
    print(index)
    if x.startswith(('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')):
        if x == 'ADJECTIVE':
            print('Enter an adjective:')
            mltext.write(x.replace(x, input()), + ' ')
        elif x == 'NOUN':
            print('Enter a noun:')
            mltext.write(x.replace(x, input()), + ' ')
        elif x == 'ADVERB':
            print('Enter an adverb:')
            mltext.write(x.replace(x, input()), + ' ')
        elif x == 'VERB':
            print('Enter a verb:')
            mltext.write(x.replace(x, input()), + ' ')
        mltext.write(x + ' ')
            
        mltext.write(x + ' ')
    elif x.startswith(('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')):
        mltext.write(x)
    elif not x.startswith(('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')) and not index == (len(splitted_text) - 1):
        mltext.write(x + ' ')
    else:
        mltext.write(x)
    '''elif x == 'ADJECTIVE':
        if x == splitted_text[len(splitted_text) - 1]:
            print('Enter an adjective:')
            mltext.write(x.replace(x, input()))
        else:
            print('Enter an adjective:')
            mltext.write(x.replace(x, input() + ' '))
            print(x)'''
    
mltext.close()
mltext = open('new_text.txt')
print(mltext.read())
    
    

# TODO: Print new text and save it to a new file.


# TODO: Change project status to "finished".
