# decrypt it game
# encrypts a random sentence
# user has to recognize patterns and decrypt it
# decrypted message always makes sense

# get the quotes
with open('quotes.txt') as qfile:
    quotes = qfile.readlines()
# quotes now contains all the messages

from random import *
# cite random somehow?

instructions = \
    '''
    Decrypt
    '''

# create functions for diff. encryptions

# ascii shift
def ascii_shift(txt,n):
    '''shifts each char in 'txt' by 'n' places on the ascii table (only printable 32>126) (modulo)
    returns shifted string
    txt -> str
    n -> int'''
    encrypted = ''
    for c in txt:
        a = ord(c)-32
        a += n
        a = a%95
        a += 32
        encrypted += chr(a)
    return encrypted

# caesar shift
def caesar_shift(txt, n):
    '''Shifts each char in 'txt' by 'n' places on the alphabetical scale
    Conserves case
    Ignores punctuation'''
    encrypted = ''
    return encrypted

# reverse
def reverse(txt):
    '''Reverses txt and returns the reversed text'''
    return txt[::-1]

# scramble (by word)
def scramble_by_word(txt):
    '''Scrambles each word in txt'''

# scramble (entire)


ciphers = [ascii_shift, caesar_shift, reverse]