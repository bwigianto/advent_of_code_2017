def generate(prev, c):
  return prev * c % 2147483647

def generate_a(prev):
  return generate(prev, 16807)

def generate_b(prev):
  return generate(prev, 48271)

def generator_func(x, gen, where):
  prev = x
  while True:
    curr = gen(prev)
    prev = curr
    if where(curr):
        yield curr

def lowest16(n):
  return "{0:016b}".format(n)[-16:]

def lowest16_match(a, b):
  return (0xffff & a) == (0xffff & b)

def count_matches(n):
  ct = 0
  a = generate_a(65)
  b = generate_b(8921)
  for i in range(n):
    if lowest16_match(a, b):
      ct += 1
    a = generate_a(a)
    b = generate_b(b)
  return ct

def count_matches2(n):
  gen_a = generator_func(512, generate_a, lambda x: x % 4 == 0)
  gen_b = generator_func(191, generate_b, lambda x: x % 8 == 0)
  ct = 0
  for i in xrange(n-1):
    a = next(gen_a)
    b = next(gen_b)
    if lowest16_match(a, b):
      ct += 1
  return ct

def part1():
  print(count_matches(40000000))

def part2():
  print(count_matches2(5000000))

print part2()
