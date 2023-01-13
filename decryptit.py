# decrypt it game
# encrypts a random sentence
# user has to recognize patterns and decrypt it
# decrypted message always makes sense

# need to format

# get the quotes
with open('quotes.txt') as qfile:
    quotes = qfile.readlines()
# quotes now contains all the messages

# format quotes (strip)
quotes = [x.strip() for x in quotes]

from random import *
# Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation.


### Begin Ciphers ###

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

### End Ciphers ###

def diff(txta,txtb):
    '''Counts the number of chars different between txta and txtb
    strips both strings
    compares the minimum length'''
    txta, txtb = txta.strip(), txtb.strip()
    d = sum(1 if a != b else 0 for a, b in zip(txta,txtb))
    return d

def fttext(func):
    '''Func to text... returns the name.
        func == function object'''
    rawf = str(func)
    if rawf[1] == 'b':
        # is builtin function
        return rawf[rawf.find('n ')+2:-1]
    else:
        return rawf[rawf.find('n ')+2:rawf.find(' at')]

# main function
def play():
    # no scramble bc it's too hard
    ciphers = [ascii_shift, caesar_shift, reverse, scramble_by_word]
    toquit = '-q'
    instructions = \
        f'''
Welcome to Decrypt It!
This game improves your cryptographic and pattern recognition skills.
You will be given a message "encrypted" in a simple "cipher".
The "ciphers" are: {' '.join([fttext(x).capitalize() for x in ciphers])}.

Your task is to decrypt the message, case sensitive.
All messages are grammatically correct and they all make sense. Most of them have valid words; some don't.

You have an infinite number of attempts. However, each attempt will be scored.
    Every correct submission is +1 point.
    Every incorrect submission is 0 points.
    Every skipped submission is -1 points.'
Enter a blank line to skip.

You are given use of commands to help you decrypt the message (parameters are seperated by spaces):
    '-i' for a hint
    '-e' for help
    '-q' to quit
    '-a num' to use ascii shift
    '-c num' to use caesar shift
    '-p' to reprint the prompt 
    

Note: Most messages end and begin with a non-space character. Spaces at the end and beginning of your submission will be ignored.

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
        encrypted = method(message, randint(-300,300))
        while message == encrypted:
            encrypted = method(message)
        prompt = f'You have {pts} point(s).\n{numtime}: |-|{encrypted}|-|'
        print(prompt)
        tries = 0
        
        while True:
            tries += 1
            # each round
            attempt = input('>: ').strip()
            
            if attempt == '':
                print('Skipped. -1 point.')
                print(f'The message was "{message}".')
                pts -= 1
                break
            
            if attempt[0] == '-': #is a command
                match attempt[1]:
                    case 'p':
                        print(prompt)
                    case 'q':
                        break
                    case 'e':
                        print('\n'.join(instructions.split('\n')[7:-2]))
                    case 'i':
                        l = randint(0,len(fttext(method))-5)
                        print(fttext(method)[l:l+4])
                        
                    case 'a' | 'c':
                        try:
                            cmd, num = attempt[1:].split(' ')
                            num = int(num)
                        except ValueError():
                            print('Error. Please enter an integer to shift.')
                            continue
                        
                        match cmd[0]:
                            case 'a':
                                print(ascii_shift(encrypted,num))
                            case 'c':
                                print(caesar_shift(encrypted,num))
                    case _:
                        print('Invalid command')
                continue
                        
            if message == attempt:
                print('Correct! +1 point.')
                pts += 1
                break

            

            print('Incorrect. 0pts.')

            if tries%8 == 0:
                print('Remember, it will make sense.')
                
        if attempt == toquit:
            print('Thank you for playing! You got',pts,'points.')
            break
        
play()
