
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

s = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'

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

print ''.join([format_hex(i) for i in out])

