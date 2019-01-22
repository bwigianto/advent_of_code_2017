import sys
import re

def print_array(a):
    for i in range(len(a)):
        s = ""
        for j in range(len(a[0])):
            s += a[i][j]
        print(s)

def boundaries(points):
    xmin = float("inf")
    xmax = - float("inf")
    ymin = float("inf")
    ymax = - float("inf")
    for x, y in points:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return (xmin, xmax, ymin, ymax)

def display(points):
    (xmin, xmax, ymin, ymax) = boundaries(points)
    out = [["." for i in range(xmin, xmax + 1)] for j in range(ymin, ymax + 1)]
    for p in points:
        out[p[1] - ymin][p[0] - xmin] = "#"
    print_array(out)

def area(points):
    (xmin, xmax, ymin, ymax) = boundaries(points)
    return (xmax - xmin + 1) * (ymax - ymin + 1)

def time_step(points, t):
    return {(p[0] + t * v[0], p[1] + t * v[1]) for p, v in points}

points = set()
for line in sys.stdin:
    match = re.search(r'position=<\s*([-0-9]+),\s*([-0-9]+)> velocity=<\s*([-0-9]+),\s*([-0-9]+)>', line)
    x = int(match.group(1))
    y = int(match.group(2))
    dx = int(match.group(3))
    dy = int(match.group(4))
    points.add(((x, y), (dx, dy)))

prev = float("inf")
t = 0
curr_area = area(time_step(points, t))
while curr_area < prev:
    t += 1
    prev = curr_area
    curr_area = area(time_step(points, t))
    print(t)

display(time_step(points, t-1))
