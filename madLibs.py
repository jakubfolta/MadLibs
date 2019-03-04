#! python3

#Mad Libs - A program which replace specified words with user inputs, save it to a new file and prints it to the console. 

import re

end_space_regex = re.compile(r'\.')
# Open text file to read and a new file to save new changed text.
'''text_file = open('textfile.txt', 'r+').read()
mltext = open('new_text.txt', 'r+')
print(text_file)
splitted_text = text_file.split()
print(splitted_text)
'''
with open('textfile.txt') as newfile:
    textlist = [x for x in newfile.read().split()]
    print(textlist)
    newtext = open('newtext.txt', 'r+')
    for x in textlist:
        if x.startswith('ADJECTIVE'):
            newtext.write(x.replace('ADJECTIVE', input('Enter an adjective: ')))
        elif x.startswith('NOUN'):
            newtext.write(x.replace('NOUN', input('Enter a noun: ')))
        elif x.startswith('ADVERB'):
            newtext.write(x.replace('ADVERB', input('Enter an adverb: ')))
        elif x.startswith('VERB'):
            newtext.write(x.replace('VERB', input('Enter a verb: ')))
        else:
            newtext.write(x)
newtext.close()
newtext = open('newtext.txt').read()
print(newtext)
    


'''# Search for specific words while looping, replace them with user input and save new text to a new file.
for x in splitted_text:
    if x.startswith('ADJECTIVE'):
        print('Enter an adjective:')
        mltext.write(x.replace('ADJECTIVE', input()))
        mltext.write(' ')
    elif x.startswith('NOUN'):
        print('Enter a noun:')
        mltext.write(x.replace('NOUN', input()))
        mltext.write(' ')
    elif x.startswith('ADVERB'):
        print('Enter an adverb:')
        mltext.write(x.replace('ADVERB', input()))
        mltext.write(' ')
    elif x.startswith('VERB'):
        print('Enter a verb:')
        mltext.write(x.replace('VERB', input()))
        mltext.write(' ')
    else:
        mltext.write(x + ' ')
'''        
#mltext.close()


# TODO: Print new text and save it to a new file.
#print(open('new_text.txt').read())


# TODO: Change project status to "finished".
