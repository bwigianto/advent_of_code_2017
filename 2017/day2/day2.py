import sys, itertools

def to_nums(line):
  return [int(x) for x in line.split("\t")]

def p1(input):
  return sum(max(arr) - min(arr) for arr in (to_nums(line) for line in input))
  
def p2(input):
  return sum(sum(x / y for (x, y) in itertools.permutations(to_nums(line), 2) if x % y == 0) for line in input)

#print p1(sys.stdin)
print p2(sys.stdin)