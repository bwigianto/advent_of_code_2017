import sys

def layer_and_depth():
    out = {}
    for line in sys.stdin:
        parts = line.split(': ')
        out[int(parts[0])] = int(parts[1])
    return out

def index(steps, n):
    q = (steps - 1)/(n-1)
    if q % 2 == 0:
        return (steps-1) % (n-1) + 1
    return n - ((steps-1) % (n-1)) 

def passed(layer_to_depth, wait):
    last = max([k for k,v in layer_to_depth.iteritems()])
    for i in xrange(last + 1):
        if i in layer_to_depth:
            d = layer_to_depth[i]
            if index(wait + i, d) == 1:
                return False
    return True

def part1():
    layer_to_depth = layer_and_depth()
    last = max([k for k,v in layer_to_depth.iteritems()])
    cost = 0
    for i in xrange(last + 1):
        if i in layer_to_depth:
            d = layer_to_depth[i]
            if index(i+1, d) == 1:
                cost += i * d
    return cost

def part2():
    layer_to_depth = layer_and_depth()
    i = 1
    while not passed(layer_to_depth, i+1):
        i += 1
    return i

print part2()
