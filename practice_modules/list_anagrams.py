#! /usr/bin/env python

from is_prime import is_prime3
from string import ascii_lowercase

def list_anagrams(word):
    prime_dict = build_alpha_dict()
    word_dict = build_word_dict(len(word))
    word = word.lower()
    mult = 1
    for i in word:
        mult *= prime_dict[i]
    try:
        return word_dict[mult]
    except KeyError:
        return word + ' is not in word list'

def build_word_dict(length):
    wordlist = open('/usr/share/dict/words', 'r')
    wordlist_lower = []
    for word in wordlist:
        word = word[:-1]
        if len(word) == length:
            wordlist_lower.append(word.lower())
    wordlist.close()

    prime_dict = build_alpha_dict()
    word_dict = {}
    for i in wordlist_lower:
        mult = 1
        for k in i:
            if k == '-':
                continue
            mult *= prime_dict[k]
        if mult in word_dict:
            word_dict[mult].append(i)
        else:
            word_dict[mult] = [i]
    return word_dict

def build_alpha_dict():
    prime_list = []
    alpha = list(ascii_lowercase)
    for i in range(2, 200):
        if is_prime3(i):
            prime_list.append(i)
            if len(prime_list) == len(alpha):
                break
    alpha_dict = dict(zip(alpha, prime_list))
    return alpha_dict


if __name__ == '__main__':
    # from timeit import timeit
    print list_anagrams('pool')
    # l = ['awork', 'korwa', 'work']
    # print timeit(stmt='list_anagrams("pool")', setup='from __main__ import list_anagrams', number=100)
