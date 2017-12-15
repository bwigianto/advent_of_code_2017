
def generate(prev, c):
  return prev * c % 2147483647

def generate_a(prev):
  return generate(prev, 16807)

def generate_b(prev):
  return generate(prev, 48271)

def lowest16(n):
  return "{0:016b}".format(n)[-16:]

def lowest16_match(a, b):
  return (0xffff & a) == (0xffff & b)

def count_matches(n):
  ct = 0
  a = generate_a(512)
  b = generate_b(191)
  for i in range(n):
    if lowest16_match(a, b):
      ct += 1
    a = generate_a(a)
    b = generate_b(b)
  return ct

def part1():
  print(count_matches(40000000))

def part2():
