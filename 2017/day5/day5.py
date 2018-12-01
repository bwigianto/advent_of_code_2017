import sys

def steps(nums):
    i = 0
    ct = 0
    while i < len(nums) and i >= 0:
        ct += 1
        next = i + nums[i]
        nums[i] += 1
        i = next
    return ct

def steps2(nums):
    i = 0
    ct = 0
    while i < len(nums) and i >= 0:
        ct += 1
        next = i + nums[i]
        if nums[i] >= 3:
            nums[i] -= 1
        else:
            nums[i] += 1
        i = next
    return ct

x = []
for line in sys.stdin:
    x.append(int(line.strip()))
print steps(x)
print steps2(x)
