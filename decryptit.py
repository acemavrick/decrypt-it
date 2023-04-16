# decrypt it game
# encrypts a random sentence
# user has to recognize patterns and decrypt it
# decrypted message always makes sense

from random import *

# Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation.
# https://docs.python.org/3/library/random.html

# get the quotes
with open('quotes.txt') as qfile:
    quotes = qfile.readlines()
# quotes now contains all the messages

# format quotes (strip)
quotes = [x.strip() for x in quotes]


### Begin Ciphers ###

# ascii shift
def ascii_shift(txt, n=None):
    """shifts each char in 'txt' by 'n' places on the ascii table (only printable 32>126) (modulo)
    returns shifted string
    txt -> str
    n -> int"""
    if not n:
        n = randint(-126, 126)

    encrypted = ''
    for c in txt:
        a = ord(c) - 32
        a += n
        a = a % 95
        a += 32
        encrypted += chr(a)
    return encrypted


# caesar shift
def caesar_shift(txt, n=None):
    """Shifts each char in 'txt' by 'n' places on the alphabetical scale
    Conserves case
    Ignores punctuation"""
    if not n:
        n = randint(-27, 27)
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
def reverse(txt, n=None):
    """Reverses txt and returns the reversed text
    n is a placeholder to enable standardization"""
    return txt[::-1]


# scramble (by word)
def scramble_by_word(txt, n=None):
    """Scrambles each word in txt
    n is a placeholder to enable standardization"""
    words = txt.split()
    scrmbled = []
    for w in words:
        scrmbled.append(scramble(w))
    return ' '.join(scrmbled)


# scramble (entire)
def scramble(txt, n=None):
    """Scrambles txt as a whole
    n is a placeholder to enable standardization"""
    a = list(txt)
    shuffle(a)
    return ''.join(a)


### End Ciphers ###

def diff(txta, txtb):
    """Counts the number of chars different between txta and txtb
    strips both strings
    compares the minimum length"""
    txta, txtb = txta.strip(), txtb.strip()
    d = sum(1 if a != b else 0 for a, b in zip(txta, txtb))
    return d


def fttext(func):
    """Func to text... returns the name.
        func == function object"""
    return func.__name__


def print_help(key):
    """prints a key:
    'ascii': prints ascii chart
    'alpha': prints alphabet chart"""
    # this saves space; Would be necessary for two functions if not one
    match key:
        case 'ascii':
            total = list(range(32, 127))
            # build 3 columns of 32
            table = []
            for i, princi in enumerate(total[:33]):
                row = [princi, total[i + 32], total[i + 62]]
                nrow = []
                for x in row:
                    a = str(x)
                    if len(a) == 2:
                        a = ' ' + a
                    nrow.append(f'{a}: "{chr(x)}"')
                row = nrow.copy()
                table.append(row)
            print('Dec: Char \t' * 3)
            # print all rows
            for row in table:
                print('\t'.join(row))
        case 'alpha':
            # print alphabet used in Caesar shift
            # case is preserved
            print("Alphabet (Case doesn't matter) ")
            print(' '.join([' ' + x for x in list('abcdefghijklmnopqrstuvwxyz')]))
            print(' '.join([(' ' if len(str(x + 1)) == 1 else '') + str(x + 1) for x in range(26)]))
        case _:
            # default case; raise error
            raise ValueError(f'{key} not in the allowed values "ascii, alpha"')


# main function
def play():
    # no scramble bc it's too hard
    # list of ciphers
    ciphers = [ascii_shift, caesar_shift, reverse, scramble_by_word]
    # scoring dictionary
    scoring = {'cor': 5, 'inc': -2, 'ski': -4, 'cmd': -.5}
    toquit = '-q'
    # because of commands, incorrect submissions are penalized (or else too easy)
    instructions = \
        f'''
Welcome to Decrypt It!
This game improves your cryptographic and pattern recognition skills.
You will be given a message "encrypted" in a simple "cipher".
The "ciphers" are: {' '.join([fttext(x).capitalize() for x in ciphers])}.

Your task is to decrypt the message, case sensitive.
All messages are grammatically correct and they all make sense. Most of them have valid words; some don't.

You have an infinite number of attempts. However, each attempt will be scored.
    Every correct submission is {scoring['cor']} points.
    Every incorrect submission is {scoring['inc']} points.
    Every skipped submission is {scoring['ski']} points.
    Every time a helper command is used (successfully) is {scoring['cmd']} points.
Enter a blank line to skip.

You are given use of commands to help you decrypt the message (parameters are seperated by spaces):
    Helper commands ({scoring['cmd']} points):
        '-i' for a hInt
        '-t [a,l]' to print a charT (replace [a,l] with either 'a' or 'l')
        '-a num' to use Ascii shift
        '-c num' to use Caesar shift
    Other (no cost):
        '-p' to rePrint the prompt 
        '-e' for hElp
        '-q' to Quit


Note: Most messages begin and end with a non-space character. Spaces at the end and beginning of your submission will be ignored.

Good luck! 
        '''
    # store points
    pts = 0
    print(instructions)
    numtime = 0
    while True:
        # main loop
        # goes on until user quits game (toquit command)

        # round the points to 4 decimal places
        pts = round(pts, 4)
        numtime += 1

        # get the message
        message = choice(quotes)
        # remove the quote so no repetition
        quotes.remove(message)
        # get the cipher to use
        method = choice(ciphers)
        # initial encryption
        encrypted = method(message, randint(-300, 300))
        # keep encrypting the message if it is the same (e.g. caesar shift by 26 is the same)
        while message == encrypted:
            encrypted = method(message)

        prompt = f'\nYou have {pts} point(s).\n{numtime}: |-|{encrypted}|-|'
        print(prompt)

        tries = 0

        while True:
            # round loop (for each encryption... until gotten right or quits)

            tries += 1

            # get attempt
            attempt = input('>: ').strip()

            # if blank (skipped)
            if attempt == '':
                print(f'Skipped. {scoring["ski"]} points.')
                print(f'The message was "{message}".')
                pts += scoring['ski']
                break  # exit round

            if attempt[0] == '-':  # is a command
                # command is structured as:
                # -[p,q,e,i,a,c] [int]
                # add 5  spaces to avoid range errors
                attempt += '     '
                # match the command's 2nd char (the actual letter)
                match attempt[1]:  # match the value after the dash
                    # no cost
                    case 'p':
                        # -p
                        print(prompt)
                    case 'q':
                        # -q
                        break
                    case 'e':
                        # -e
                        # print the scoring guidelines and the command key
                        print('\n'.join(instructions.split('\n')[7:-2]))

                    # cost
                    case 'i' | 'a' | 'c' | 't':
                        # the commands in these cases use up points
                        # run match again
                        # take of points at end to account for errors
                        # if a command is not run successfully, points will not be taken off
                        match attempt[1]:

                            case 'i':
                                # -i
                                # print 4 letters of the name of the cipher method
                                l = randint(0, len(fttext(method)) - 5)
                                print(fttext(method)[l:l + 4])

                            case 't':
                                # -t [a,l]
                                # print chart based on the next value
                                match attempt[3]:
                                    # 3rd of command
                                    # e.g. -t a
                                    #         ^
                                    case 'l':
                                        print_help('alpha')
                                    case 'a':
                                        print_help('ascii')
                                    case _:
                                        # default
                                        # none match... invalid second letter
                                        print(
                                            'Error. Please enter either "a" or "l" after "-t " for Ascii and alphabet \
                                            charts, respectively')
                                        continue

                            case 'a' | 'c':
                                # -a or -c
                                # need to get the number
                                try:
                                    # try to split by spaces
                                    asplit = attempt[1:].split(' ')
                                    cmd, num = asplit[:2]
                                    # try to integer the number
                                    num = int(num)
                                except ValueError:
                                    print('Error. Please enter an integer to shift.')
                                    continue

                                match cmd[0]:
                                    # now we have the integer, classify based on the command
                                    case 'a':
                                        # -a _
                                        # shift it and print it
                                        print(ascii_shift(encrypted, num))
                                    case 'c':
                                        # -c _
                                        # shift it and print it
                                        print(caesar_shift(encrypted, num))
                        # if it reaches here command was successful. Take off points.
                        print(f'Helper command used: {scoring["cmd"]} points.')
                        pts += scoring['cmd']

                    # bad command
                    case _:
                        # default case
                        # if nothing works, print invalid command
                        print('Invalid command')
                # don't evaluate further than the command, so continue
                continue

            ### Scoring ###

            # the attempt is correct
            if message == attempt:
                print(f'Correct! {scoring["cor"]} point.')
                pts += scoring['cor']
                break

            # reaching here means that it is incorrect
            print(f'Incorrect. {scoring["inc"]}.')
            pts += scoring['inc']

            # typo checking. if it is a typo then suggest it and give back points
            # typo is when the number of characters wrong is <= num words
            #  and both are the same length
            if len(attempt) == len(message):
                # the messages need to be the same length
                # if it isn't chances are low that there is a typo
                # also if it isn't then typo count will be incorrect

                # get num different
                numtypos = diff(attempt, message)
                wordcount = len(message.split(' '))
                # if too many typos then probably not typos
                if numtypos > wordcount:
                    continue

                # calculate how much to give back for each typo based on wordcount
                # cannot give back more than points negated for incorrect
                value = abs(scoring['inc'] / wordcount)

                # inverse proportion
                givenback = value * wordcount / numtypos
                givenback = round(givenback, 4)  # rounds to be nice
                pts += givenback
                print(f'It seems like you have {numtypos} typos, so you will be given back {givenback} points.')
                continue

            # every 8 tries, remind that it will make sense
            if tries % 8 == 0:
                print('Remember, it will make sense.')

        # want to quit
        if attempt[:2] == toquit:
            print('Thank you for playing! You got', pts, 'points.')
            break


if __name__ == '__main__':
    play()
