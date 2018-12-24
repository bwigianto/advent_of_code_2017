import sys

def squares(x, y, w, h):
    out = set()
    for i in range(x, x + w):
        for j in range(y, y + h):
            out.add((i, j))
    return out

used = set()
intersections = set()

for line in sys.stdin:
    parts = line.split(" ")
    id = parts[0]
    x = int(parts[2].split(",")[0])
    y = int(parts[2].split(",")[1].split(":")[0])
    w = int(parts[3].split("x")[0])
    h = int(parts[3].split("x")[1])
    current_squares = squares(x, y, w, h)
    current_intersections = current_squares.intersection(used)
    intersections = intersections.union(current_intersections)
    used = used.union(current_squares)

with open("input.txt", "r") as f:
    for line in f:
        parts = line.split(" ")
        id = parts[0]
        x = int(parts[2].split(",")[0])
        y = int(parts[2].split(",")[1].split(":")[0])
        w = int(parts[3].split("x")[0])
        h = int(parts[3].split("x")[1])
        if len(squares(x, y, w, h).intersection(intersections)) == 0:
            print(id)
            break
