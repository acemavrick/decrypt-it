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


### caesar shift left

# create functions for diff. encryptions

# ascii shift
def ascii_shift(txt,n = None):
    '''shifts each char in 'txt' by 'n' places on the ascii table (only printable 32>126) (modulo)
    returns shifted string
    txt -> str
    n -> int'''
    if n == None:
        n = randint(-126,126)
        
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
        n = randint(-27,27)
    encrypted = ''
    base = ord('a')
    for l in txt:
        if l.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            encrypted += l
            continue
        ll = l.lower()
        waslow = l == ll
        a = ord(ll)
        a -= base
        a += n
        a %= 26
        a += base
        nl = chr(a)
        nl = nl if waslow else nl.upper()
        encrypted += nl
    return encrypted
    

# reverse
def reverse(txt,n = None):
    '''Reverses txt and returns the reversed text
    n is a placeholder to enable standardization'''
    return txt[::-1]

# scramble (by word)
def scramble_by_word(txt,n = None):
    '''Scrambles each word in txt
    n is a placeholder to enable standardization'''
    words = txt.split()
    scrmbled = []
    for w in words:
        scrmbled.append(scramble(w))
    return ' '.join(scrmbled)
    
# scramble (entire)
def scramble(txt,n = 0):
    '''Scrambles txt as a whole
    n is a placeholder to enable standardization'''
    a = list(txt)
    shuffle(a)
    return ''.join(a)

def play():
    ciphers = [ascii_shift, caesar_shift, reverse, scramble_by_word, scramble]
    instructions = \
        '''
        Welcome to Decrypt It!
        This game improves your cryptographic and pattern recognition skills.
        You will be given a message encrypted in a simple cipher.
        ##maybe put ciphers??
        Your task is to decrypt the message, case sensitive.
        Every message correct is +1 point. Every incorrect is -1 point. Every skipped is 0 points.
        Enter a blank line to skip.
        Enter 'qx' to quit.
        #put h for hints
        Good luck!
        '''
    pts = 0
    print(instructions)
    while True:
        pass
        break
