import sys

n = 2
steps = 1
def roots(nodes_to_parents):
    out = set()
    for node, parents in nodes_to_parents.items():
        parent = parents[0]
        while parent in nodes_to_parents:
            parent = nodes_to_parents[parent][0]
        out.add(parent[0])
    return list(out)

nodes_to_children = {}
nodes_to_parents = {}
nodes_to_work = {}
for line in sys.stdin:
    parts = line.split(" ")
    letter = parts[1]
    child_letter = parts[7]
    if letter in nodes_to_children:
        nodes_to_children[letter].append(child_letter)
    else:
        nodes_to_children[letter] = [child_letter]
    if child_letter not in nodes_to_children:
        nodes_to_children[child_letter] = []
    if child_letter in nodes_to_parents:
        nodes_to_parents[child_letter].append(letter)
    else:
        nodes_to_parents[child_letter] = [letter]
    if letter not in nodes_to_parents:
        nodes_to_parents[letter] = []
    if letter not in nodes_to_work:
        nodes_to_work[letter] = ord(letter) - 64
    if child_letter not in nodes_to_work:
        nodes_to_work[child_letter] = ord(child_letter) - 64

def fulfilled(node, visited, nodes_to_parents):
    if node not in nodes_to_parents:
        return True
    return all(x in visited for x in nodes_to_parents[node])

def ready(to_visit, visited, nodes_to_parents):
    out = []
    for i in range(len(to_visit)):
        node = to_visit[i]
        if fulfilled(node, visited, nodes_to_parents):
            out.append(to_visit.pop(i))
    return out

roots = roots(nodes_to_parents)
print(roots)
to_visit = sorted(roots)
order = []
visited = set(roots)
while len(to_visit) > 0:
    curr = ready(to_visit, visited, nodes_to_parents)
    visited.add(curr)
    order.append(curr)
    for child in nodes_to_children[curr]:
        if child not in visited and child not in set(to_visit):
            to_visit.append(child)
    to_visit = sorted(to_visit)

print(''.join(order))
