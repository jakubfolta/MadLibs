#! python3

# madlib-solidifying.py - A program which replace specified words with user inputs, save it to a new file and prints it to the console.

# Create variable with words to exchange.
words = ['ADJECTIVE', 'ADVERB', 'VERB', 'NOUN']

# Open file with text to check.
with open('textfile.txt') as textfile:
# Split text.
    splitted_text = textfile.read().split()
    print(splitted_text)

# Open new file to save new text and use loop to exchange specified words.
with open('changedtext.txt', 'w') as newtext:
    for x in splitted_text:
        for y in words:
            if x.startswith(y):
                word = input('Please enter ' + y.lower() + ':' + '\n')
                newtext.write(x.replace(y, word) + ' ')
                break
        else:
            newtext.write(x + ' ')

with open('changedtext.txt') as newtext:
    content = newtext.read()
    print(content)

# TODO: Loop through the file and exchange specified words.
# TODO: Save new changed text to a new file.
