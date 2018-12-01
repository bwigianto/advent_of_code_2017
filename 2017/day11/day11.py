import sys

def step(s):
    if s == 'n':
        return [0, 2]
    if s == 's':
        return [0, -2]
    if s == 'ne':
        return [1, 1]
    if s == 'se':
        return [1, -1]
    if s == 'nw':
        return [-1, 1]
    if s == 'sw':
        return [-1, -1]

def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def closest_cardinal(x, y):
    dirs = [[1, 1], [1, -1], [-1, 1], [-1, -1], [0, 2], [0, -2]]
    min_dist = sys.maxint 
    min_dir = None
    for dir in dirs:
        curr_dist = dist(add(dir, x), y)
        if curr_dist < min_dist:
            min_dist = curr_dist
            min_dir = dir
    return min_dir

def steps_away(x, y):
    ct = 0
    curr = x
    while dist(curr, y) != 0:
        curr = add(curr, closest_cardinal(curr, y))
        ct += 1
    return ct


#input = 'ne,ne,sw,sw'
#input = 'ne,ne,ne'
#input = 'ne,ne,s,s'
#input = 'se,sw,se,sw,sw'
input = None
for line in sys.stdin:
    input = line.strip()
start = [0, 0]
curr = [0, 0]
dirs = [step(d) for d in input.split(',')]
max_dist = 0
for d in dirs:
    curr = add(curr, d)
    max_dist = max(steps_away(curr, start), max_dist)
    print max_dist
print max_dist
#print ct
#print closest_cardinal([0, 0],[3, 1])
#print steps_away(start, curr)
