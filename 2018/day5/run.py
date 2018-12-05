import os
import collections

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
   
#with open('input.txt', 'r') as myfile:
#    word = myfile.read().replace('\n', '')
#    x = decompose(word)
#    print(x)
#    print(len(x))
#
#print(decompose(word))
