import sys, itertools, collections

def valid(line):
    words = {}
    for word in line.split(' '):
        if word.strip() in words:
            return False
        words[word.strip()] = True
    return True

def anagram(a, b):
   return collections.Counter(a) == collections.Counter(b) 

def valid2(line):
    for (a, b) in itertools.combinations(line.split(' '), 2):
        a = a.strip()
        b = b.strip()
        if anagram(a.strip(), b.strip()):
            return False
    return True

tot = 0
for line in sys.stdin:
    if valid2(line):
        tot += 1
print tot
