#! /usr/bin/env python3
''' Pig Latin Converter'''
import time
import string

# Print the title and introduction
def print_title():
    ''' Function prints the title of the program
    Takes no arguments '''

    title = 'Welcome to the Amazing Pig Latin Converter!!'
    spaces = ' ' * int(((80 - (len(title)+2)) / 2))
    print('-'*80)
    print(f'|{spaces}{title}{spaces}|')
    print('-' * 80)

# Get the phrase from the user
def get_phrase():
    ''' Function that asks the user for a phase to Convert
        Takes not arguments returns str()'''
    return input('What phrase would you like to convert?\n\n')

# Convert phrase into pig latin
def convert_phrase():
    ''' Function retutns a string in pig latin
        takes no arguments'''
    phrase = get_phrase()
    word_list = phrase.split()
    pig_latin_list = []
    punc = ''
    for i in word_list:
        punc = ''
        if i[-1] in string.punctuation:
            punc = i[-1]
            i = i[:-1]
        if i[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            i = i+'way'
            pig_latin_list.append(i)
        else:
            i = i[1:] + i[0] + 'ay'
            pig_latin_list.append(i)

    pig_latin = ' '.join(pig_latin_list) + punc
    status_screen()
    return pig_latin

def status_screen():
    ''' Visual Flair'''
    spot = 0
    forward = True
    for i in range(160):
        if forward:
            spot = spot + 1
        else:
            spot = spot - 1
        if spot >= 80:
            forward = False
        elif spot <= 0:
            forward = True

        line = '0' * 80
        print(line[:spot]+'*'+ line[spot+1:])
        time.sleep(.007)
    print('\n')

print_title()
while True:
    print(convert_phrase()+'\n')
    play_again = input('Do you want to play again? (n to quit) ')
    print('\n')
    if play_again.lower() == 'n':
        break
