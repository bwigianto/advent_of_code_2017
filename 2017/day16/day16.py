import sys

def spin(s, n):
    n = n % len(s)
    if n == 0:
        return s
    return s[-n:] + s[0:len(s)-n]

def exchange(s, i, j):
    arr = list(s)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return ''.join(arr)

def swap(s, x, y):
    i = s.index(x)
    j = s.index(y)
    return exchange(s, i, j)

def spin_tests():
    assert spin('abcd', 0) == 'abcd'
    assert spin('abcd', 1) == 'dabc'
    assert spin('abcd', 2) == 'cdab'
    assert spin('abcd', 5) == 'dabc'

def exchange_tests():
    assert exchange('abcd', 0, 1) == 'bacd'
    assert exchange('abcd', 0, 3) == 'dbca'

def swap_tests():
    assert swap('abcd', 'a', 'b') == 'bacd'
    assert swap('abcd', 'a', 'd') == 'dbca'

#spin_tests()
#exchange_tests()
#swap_tests()

def func(instr, s):
    if instr[0] == 's':
        return spin(s, int(instr[1:]))
    parts = instr[1:].split('/')
    if instr[0] == 'x':
        return exchange(s, int(parts[0]), int(parts[1]))
    if instr[0] == 'p':
        return swap(s, parts[0], parts[1])

def part1():
    s = 'abcdefghijklmnop'
    for line in sys.stdin:
        pass
    instructions = [l.strip() for l in line.split(',')]
    for i in xrange(1000000000):
        for instr in instructions:
            s = func(instr, s)
    return s
'''
abcdefghijklmnop
kpfonjglcibaedhm
'''
def part2():
    s = 'abcdefghijklmnop'
    for line in sys.stdin:
        pass
    instructions = [l.strip() for l in line.split(',')]
    seen = {s: 0}
    for i in xrange(1000000000):
        for instr in instructions:
            s = func(instr, s)
        print i+1,s
        if s in seen:
            print s,seen[s],(i+1)
            return None
        else:
            seen[s] = i+1
        
    return s



print part2()
