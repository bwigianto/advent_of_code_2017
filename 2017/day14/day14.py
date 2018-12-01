
def reversed(arr, start, length):
  out = []
  for i in xrange(length):
    out.append(arr[(start + i) % len(arr)])
  return out[::-1]

def update(arr, start, length, skip):
  revd = reversed(arr, start, length)

  for i in xrange(len(revd)):
    arr[(i+start) % len(arr)] = revd[i]

  return (arr, (start + length + skip) % len(arr), skip + 1)

def format_hex(s):
  out = hex(s)
  if len(out) == 3:
    return '0' + out[-1]
  return out[2:]

def knot_hash(s):
  arr = range(256)
  skip = 0
  curr = 0
  input = [ord(i) for i in s] + [17, 31, 73, 47, 23]
  for j in xrange(64):
    for i in input:
      (arr, curr, skip) = update(arr, curr, i, skip)
  
  out = []
  for i in xrange(16):
    temp = arr[16 * i]
    for j in xrange(1, 16):
      temp ^= arr[16 * i + j]
    out.append(temp)
  
  return ''.join([format_hex(i) for i in out])

def hex_str_to_bits(s):
  return "".join(["{0:04b}".format(int(c, 16)) for c in s])

def count_ones(s):
  return sum(int(c) for c in s if c == '1')

def count_ones_in_knot_hash(s):
  return sum(count_ones(word) for word in [hex_str_to_bits(row) for row in [knot_hash(s + '-' + str(i))  for i in xrange(128)]])

def p1():
  print count_ones_in_knot_hash('hfdlxzhv')

def matrix(s):
  A = [[0 for x in xrange(128)] for y in xrange(128)]
  for i in xrange(128):
    bitstr = hex_str_to_bits(knot_hash(s + '-' + str(i)))
    for j in xrange(128):
      A[i][j] = int(bitstr[j])
  return A

def valid(i, j):
  return i >= 0 and i < 128 and j >= 0 and j < 128

def neighbors(A, i, j, visited):
  to_visit = [(i,j)]
  v = set()
  while len(to_visit) > 0:
    curr = to_visit.pop()
    (x, y) = curr
    if not valid(x, y) or A[x][y] == 0 or curr in v or curr in visited:
      v.add(curr)
      continue
    else:
      for neighbor in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        to_visit.append(neighbor)
      v.add(curr)
  return v 

def p2():
  s = 'hfdlxzhv'
  A = matrix(s)
  visited = set()
  ct = 0
  for i in xrange(128):
    for j in xrange(128):
      if A[i][j] == 0 or (i,j) in visited:
        continue
      else:
        visited |= neighbors(A, i, j, visited)
        ct += 1
  return ct      


print p2()
