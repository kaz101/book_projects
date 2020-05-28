#! venv/bin/python3

def open_file(file):
    ''' Function opens a file and stores lines in a list
        takes a file path as argument
        returns a list'''
    try:
        with open(file) as in_file:
            lines = in_file.readlines()
            lines = [x.strip('\n') for x in lines]
            lines = [x.lower() for x in lines]
            return lines
    except IOError as e:
        print(e, 'File not found')

def check_palindromes(word_list):
    ''' Function checks for palindroms takes a word_list
        of words for argument returns a list'''
    palindroms = []
    for i in word_list:
        backwards = i[::-1]
        if i == backwards and len(i) > 1:
            palindroms.append(backwards)
    return palindroms







word_list = open_file('/usr/share/dict/words')
palindroms = check_palindromes(word_list)
print(*palindroms, sep='\n')
