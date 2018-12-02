import os
import collections

def twos_and_threes(line):
    counter = collections.Counter(line)
    twos = 0
    threes = 0
    for c in counter:
        if counter[c] == 2:
            twos = 1
        if counter[c] == 3:
            threes = 1
    return (twos, threes)


def checksum(filename):
    nums = []
    with open(filename, 'r') as f:
        twos = 0
        threes = 0
        for line in f:
            (x, y) = twos_and_threes(line)
            twos += x
            threes += y
    return twos * threes

def diff(s1, s2):
    s = 0
    for c in range(len(s1)):
        if s1[c] != s2[c]:
            s += 1
    return s

def common(filename):
    letters = []
    with open(filename, 'r') as f:
        letters = [line for line in f]
    first = None
    sec = None
    mindiff = 10000
    for w1 in range(len(letters)):
        for w2 in range(w1 + 1, len(letters)):
            d = diff(letters[w1], letters[w2])
            if d < mindiff:
                mindiff = d
                first = letters[w1]
                sec = letters[w2]
    return (mindiff, first, sec)


#print(checksum('input.txt'))
#print(checksum('sample.txt'))
#print(diff('abcde', 'accdf'))
#print(common('sample.txt'))
print(common('input.txt'))
            
