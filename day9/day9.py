'''
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.

{{{{}}, {{{}}, {{}, {}}}}} 1
{{{}}, {{{}}, {{}, {}}}} 2
[{{}}, {{{}}, {{}, {}}}]
{{}} 3
{} 4
{{{}}, {{}, {}}} 3
{{}}, {{}, {}} 4
{{}}
{}
{{}, {}}
{}
{}

{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
'''
import sys

def score(s, val):
  if s == '':
    return 0

  stack = []
  curr = ''
  tot = 0
  for c in s:
    if c == '{':
      stack.append('{')
    elif c == '}':
      stack.pop()
    curr += c
    if len(stack) == 0:
      print curr, val
      if curr != ',':
        tot += val + score(curr[1:(len(curr)-1)], val + 1)
      curr = ''
  return tot

def sanitize(s):
  prev = None
  ignoring = False
  undo = False
  out = ''
  removed = 0
  for c in s:
    if undo:
      undo = False
      continue
    if c == '!':
      undo = True
      continue
    elif c == '>':
      if ignoring:
        ignoring = False
    elif c == '<':
      if ignoring:
        removed += 1
      ignoring = True
    elif not ignoring:
      out += c
    else:
      removed += 1
  return (out, removed)

def overall_score(s):
  out, removed = sanitize(s)
  return (score(out, 1), removed)

# print score('{}', 1)
# print score('{{}}', 1)
# print score('{{{}}}', 1)
# print score('{{{},{},{{}}}}', 1)

# print score('{,,,}', 1)


# print sanitize('{<a>,<a>,<a>,<a>}')
# print sanitize('{{<a>},{<a>},{<a>},{<a>}}')

# print overall_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')
# print overall_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')
# print overall_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')
# print score('{{{},{},{{}}}}', 1)
# print score('{{{{}}, {{{}}, {{}, {}}}}}'.replace(' ', ''), 1)



for line in sys.stdin:
  print overall_score(line.strip())