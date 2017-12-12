import sys

def ids_in_same_group(id, id_to_neighbors):
    visited = set()
    ct = 0
    to_visit = [id]
    while len(to_visit) > 0:
        
        curr = to_visit.pop()
        if curr in visited:
            continue
        visited.add(curr)
        ct += 1
        for neighbor in id_to_neighbors[curr]:
            to_visit.append(neighbor)
    return visited

def key_and_val(line):
    parts = line.split(' <-> ')
    neighbors = [int(x) for x in parts[1].split(',')]
    return int(parts[0]), neighbors

id_to_neighbors = {}
for line in sys.stdin:
    k, v = key_and_val(line)
    id_to_neighbors[k] = v

def part1():
    print len(ids_in_same_group(0, id_to_neighbors))

def part2():
    visited = set()
    ct = 0
    for id in id_to_neighbors:
        if id in visited:
            continue
        else:
            ct += 1
            visited = visited | ids_in_same_group(id, id_to_neighbors)
    return ct

print part2()

