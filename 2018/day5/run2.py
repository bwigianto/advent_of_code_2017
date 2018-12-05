import os
from collections import Counter

word = "dabAcCaCBAcCcaDA"

def interact(c1, c2):
    return c1 != c2 and c1.lower() == c2.lower()

def trim(s):
    out = ""
    i = 0
    curr = 1
    while curr < len(s):
        if not interact(s[i], s[i+1]):
            out += s[i]
            i += 1
            curr += 1
        else:
            i += 2
            curr += 2

    if i == len(s) - 1:
        out += s[i]
    return out

def decompose(word):
    prev = None
    while prev != word:
        prev = word
        word = trim(word)
    return word

def letters(word):
    return [k for k in Counter(word)]

def remove(word, c):
    return word.replace(c.upper(), '').replace(c.lower(), '')

def score(word, c):
    return len(decompose(remove(word, c)))

def best_score(word):
    min_score = len(word) + 1
    for letter in letters(word):
        curr_score = score(word, letter)
        if curr_score < min_score:
            min_score = curr_score
    return min_score



with open('input.txt', 'r') as myfile:
    word = myfile.read().replace('\n', '')
    print(best_score(word))
