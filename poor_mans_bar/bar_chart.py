#! venv/bin/python3
''' Sentance Analyzer'''
import time
def print_title():
    '''Prints the title of the game takes no arguments'''
    for i in range(100):
        print()
    title = 'The Super Fantastic Sentance Analyzer!!!'
    spaces = ' ' * ((80 - (len(title)+2)) // 2)
    print('-'*80)
    time.sleep(.2)
    print(f'|{spaces}{title}{spaces}|')
    time.sleep(.2)
    print('-' * 80)
    for i in range(10):
        time.sleep(.1)
        print()

def count_letters(sentence):
    '''counts the number of letters and returns a dictonary of lists'''
    main_dict = {}
    for i in sentence:
        if i not in main_dict.keys() and i != ' ':
            main_dict[i] = []
            for j in sentence:
                if j == i:
                    main_dict[i].append(j)
    return main_dict

def print_results(main_dict):
    '''prints the results to the screen'''
    for key in main_dict.keys():
        print(key, main_dict[key],len(main_dict[key]))
        time.sleep(.1)


print_title()
sentence = input('Gimmie a sentence will ya? ').lower()
main_dict = count_letters(sentence)
print_results(main_dict)
