# decrypt it game
# encrypts a random sentence
# user has to recognize patterns and decrypt it
# decrypted message always makes sense

# get the quotes
with open('quotes.txt') as qfile:
    quotes = qfile.readlines()
# quotes now contains all the messages

# format quotes (strip)
quotes = [x.strip() for x in quotes]

from random import *
# Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation.


def count_diff(txta,txtb):
    '''Counts the number of chars different between txta and txtb
    strips both strings
    compares the minimum length'''
    txta, txtb = txta.strip(), txtb.strip()
    diff = 0
    l = min(len(txta),len(txtb))
    for i in range(l):
        if txta[i] != txtb[i]:
            diff += 1
    return diff

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
def scramble(txt,n = None):
    '''Scrambles txt as a whole
    n is a placeholder to enable standardization'''
    a = list(txt)
    shuffle(a)
    return ''.join(a)

def play():
    ciphers = [ascii_shift, caesar_shift, reverse, scramble_by_word, scramble]
    toquit = '.q'
    instructions = \
        f'''
Welcome to Decrypt It!
This game improves your cryptographic and pattern recognition skills.
You will be given a message "encrypted" in a simple "cipher".

##maybe put ciphers??

Your task is to decrypt the message, case sensitive.
All messages are grammatically correct and they all make sense. Most of them have valid words; some don't.

You have an infinite number of attempts. However, each attempt will be scored.
Every correct submission is +1 point. Every incorrect submission is 0 points. Every skipped submission is -1 points.
Enter a blank line to skip.

Note: Most messages end and begin with a non-space character. Spaces at the end and beginning of your submission will be ignored.

Enter '{toquit}' to quit.

#put h for hints

Good luck!
        
        '''
    pts = 0
    print(instructions)
    numtime = 0
    while True:
        # main loop
        numtime += 1
        message = choice(quotes)
        # remove the quote so no repetition
        quotes.remove(message)
        method = choice(ciphers)
        encrypted = method(message)
        while message == encrypted:
            encrypted = method(message)
        print()
        print('You have',pts,'point(s).')
        print(f'{numtime}: |-|{encrypted}|-|')
        
        while True:
            # each round
            tries = 0
            attempt = input('>: ').strip()
            print()
            
            if attempt == toquit:
                break
                
            if message == attempt:
                print('Correct! +1 point.')
                pts += 1
                break

            if attempt == '':
                print('Skipped. -1 point.')
                pts -= 1
                break

            print('Incorrect. 0pts.')
            numdiff = count_diff(message, attempt)

            if tries%5 == 0:
                print('Remember, it will make sense.')
            tries += 1
                
        if attempt == toquit:
            print('Thank you for playing! You got',pts,'points.')
            break
        print()
        
play()
