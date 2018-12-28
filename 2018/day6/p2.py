import sys


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

assert dist(1, 3, 5, 9) == 10

def closest(points, x, y):
    min_dist = float("inf")
    min_point = None
    for i, j in points:
        d = dist(i, j, x, y)
        if d == min_dist:
            min_point = None
        if d < min_dist:
            min_dist = d
            min_point = (i, j)
    return min_point

assert closest([(0, 0), (1, 1), (0, 1), (1, 0)], 2, 2) == (1, 1)
assert closest([(0, 0), (1, 1), (0, 1), (1, 0)], -1, -1) == (0, 0)
assert closest([(1, 1), (5, 5)], 3, 3) == None

def border(x, y, minX, maxX, minY, maxY):
    return x == minX or x == maxX or y == minY or y == maxY

def total_dist(points, x, y):
    return sum(dist(i, j, x, y) for i, j in points)

assert total_dist([(1, 1), (5, 5)], 3, 3) == 8

minX = float("inf")
maxX = - float("inf")
minY = float("inf")
maxY = - float("inf")
points = set()
for line in sys.stdin:
    parts = line.split(",")
    x = int(parts[0])
    y = int(parts[1])
    if x > maxX:
        maxX = x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y
    points.add((x, y))

total = 0
for x in range(minX, maxX + 1):
    for y in range(minY, maxY + 1):
        d = total_dist(points, x, y)
        if d < 10000:
            total += 1

print(total)
