import os

def find_first_repeat(filename):
    nums = []
    with open(filename, 'r') as f:
        nums = [int(line) for line in f]
    i = 0
    t = 0
    seen = set()
    while True:
        t += nums[i]
        i = (i + 1) % len(nums)
        if t in seen:
            return t
        seen.add(t)

print(find_first_repeat('input.txt'))
            
