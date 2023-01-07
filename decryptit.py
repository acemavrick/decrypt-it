# decrypt it game
# encrypts a random sentence
# user has to recognize patterns and decrypt it
# decrypted message always makes sense

# get the quotes
with open('quotes.txt') as qfile:
    quotes = qfile.readlines()
# quotes now contains all the messages

from random import *
# Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation.

instructions = \
    '''
    Decrypt
    '''

### caesar shift left

# create functions for diff. encryptions

# ascii shift
def ascii_shift(txt,n = None):
    '''shifts each char in 'txt' by 'n' places on the ascii table (only printable 32>126) (modulo)
    returns shifted string
    txt -> str
    n -> int'''
    if n == None:
        n = randint(0,126)
        
    encrypted = ''
    for c in txt:
        a = ord(c)-32
        a += n
        a = a%95
        a += 32
        encrypted += chr(a)
    return encrypted

# caesar shift
def caesar_shift(txt, n=None):
    '''Shifts each char in 'txt' by 'n' places on the alphabetical scale
    Conserves case
    Ignores punctuation'''
    if n == None:
        n = randint(0,27)
    encrypted = ''
    for l in txt:
        if l.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            encrypted += l
            continue
        encrypted += '+'
        pass
    return encrypted
    

# reverse
def reverse(txt):
    '''Reverses txt and returns the reversed text'''
    return txt[::-1]

# scramble (by word)
def scramble_by_word(txt):
    '''Scrambles each word in txt'''
    words = txt.split()
    scrmbled = []
    for w in words:
        scrmbled.append(scramble(w))
    return ' '.join(scrmbled)
    
# scramble (entire)
def scramble(txt):
    '''Scrambles txt as a whole'''
    a = list(txt)
    shuffle(a)
    return ''.join(a)


ciphers = [ascii_shift, caesar_shift, reverse, scramble_by_word, scramble]
