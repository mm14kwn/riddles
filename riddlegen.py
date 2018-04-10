#!python3
import numpy as np
from itertools import count as icount


def ordinal(n):
    """
    returns the ordinal of a number (ie 1>1st, 2>2nd etc)
    """
    import math
    out = "%d%s" % (
        n,
        "tsnrhtdd" [(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])
    return out


def wlists(character, word_list):
    """
    generates list of words with and without character from word_list
    """
    character = character.casefold()
    words_with_letter = [word for word in word_list if character in word]
    words_without_letter = [
        word for word in word_list if character not in word
    ]
    return words_with_letter, words_without_letter


def gen(input_string=None, dictionary='./en', debug=False):
    """
    generates a 'my first is in x but not in y' type riddle
    from an arbitrary string.
    Wordlist is from dictionary. - can specify
    """

    with open(dictionary, 'r') as f:
        word_list = f.read().split('\n')
        word_list = list(filter(None, word_list))
        word_list = [word.casefold() for word in word_list]
    if input_string is None:
        input_string = input('please enter string to generate riddle from')
    if not isinstance(input_string, str):
        raise ValueError('Input is not string')
    firstword = []
    secondword = []
    for character in input_string:
        if character.isalpha():
            wwl, wwol = wlists(character, word_list)
            wwl2 = []
            wwol2 = []
            for otheralpha in 'abcdefghijklmnopqrstuvwxyz'.replace(character,
                                                                   ''):
                for wi, wo in zip(wwl, wwol):
                    if otheralpha not in wi or otheralpha in wo:
                        wwl2.append(wi)
                        wwol2.append(wo)
            if len(wwl2) == 0 or len(wwol2) == 0:
                if debug:
                    print('words with = ', wwl2)
                    print('words without = ', wwol2)
                raise ValueError(
                    'No words in the dictionary work for letter {0}'.format(
                        character))

            wind = np.random.randint(0, len(wwl2))
            woind = np.random.randint(0, len(wwol2))
            firstword.append(wwl2[wind])
            secondword.append(wwol2[woind])
        else:
            firstword.append(None)
            secondword.append(None)

    for count, fw, sw, ch in zip(icount(), firstword, secondword,
                                 input_string):
        if debug:
            print(count, fw, sw, ch)
        if fw is None or sw is None:
            rstring = ch
        else:
            rstring = 'My {0} is in {1} but not in {2}\n'.format(
                ordinal(count + 1), fw, sw)
        print(rstring)
