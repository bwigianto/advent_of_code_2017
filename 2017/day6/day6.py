import sys
import operator
def rotate(arr):
    index, value = max(enumerate(arr), key=operator.itemgetter(1))
    arr[index] = 0
    for i in xrange(value):
        arr[(index + i + 1) % len(arr)] += 1
    return arr

def rotate_until_loop(arr):
    seen = {}
    ct = 0
    while str(arr) not in seen:
        seen[str(arr)] = True
        arr = rotate(arr)
        ct += 1
    return ct

def rotate_until_loop2(arr):
    seen = {}
    ct = 0
    while str(arr) not in seen:
        ct += 1
        seen[str(arr)] = ct
        arr = rotate(arr)
    return ct - seen[str(arr)] + 1

input = [4,  10,  4,   1,   8,   4,   9,   14,  5,   1,   14,  15,  0,   15,  3,   5]

print rotate_until_loop(input)
print rotate_until_loop2(input)
