#! python3

#Mad Libs - A program which replace specified words with user inputs, save it to a new file and prints it to the console.

import re

# Open text file to read and a new file to save new changed text.
with open('textfile.txt') as newfile:
    textlist = newfile.read().split()
    print(textlist)
newtext = open('newtext.txt', 'w')

# Search for specific words while looping, replace them with user input and save new text to a new file.
for x in textlist:
    if x.startswith('ADJECTIVE'):
        newtext.write(x.replace('ADJECTIVE', input('Enter an adjective: ')))
        newtext.write(' ')
    elif x.startswith('NOUN'):
        newtext.write(x.replace('NOUN', input('Enter a noun: ')))
        newtext.write(' ')
    elif x.startswith('ADVERB'):
        newtext.write(x.replace('ADVERB', input('Enter an adverb: ')))
        newtext.write(' ')
    elif x.startswith('VERB'):
        newtext.write(x.replace('VERB', input('Enter a verb: ')))
        newtext.write(' ')
    else:
        newtext.write(x + ' ')
newtext.close()

'''newtext = open('newtext.txt')
stri = newtext.read()
print(stri)
stri = re.sub(r'\s+$', '', stri)
newtext.close()
print(stri)
with open('newtext.txt', 'w') as newfile:
    newfile.write(stri)
   '''

# Print new text and save it to a new file.
with open('newtext.txt') as temp_file:
    stripped_file = ''.join([x.strip() for x in temp_file.readlines()])
    print(stripped_file)
with open('newtext.txt', 'w') as file:
    file.write(stripped_file)
