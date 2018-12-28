import sys

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
for line in sys.stdin:
    parts = line.split(" ")
    letter = parts[1]
    child_letter = parts[7]
    if letter in nodes_to_children:
        nodes_to_children[letter].append(child_letter)
    else:
        nodes_to_children[letter] = [child_letter]
    if child_letter in nodes_to_parents:
        nodes_to_parents[child_letter].append(letter)
    else:
        nodes_to_parents[child_letter] = [letter]

def fulfilled(node, visited, nodes_to_parents):
    if node not in nodes_to_parents:
        return True
    return all(x in visited for x in nodes_to_parents[node])

def first_fulfilled(to_visit, visited, nodes_to_parents):
    for i in range(len(to_visit)):
        node = to_visit[i]
        if fulfilled(node, visited, nodes_to_parents):
            return to_visit.pop(i)


roots = roots(nodes_to_parents)
to_visit = sorted(roots)
order = []
visited = set(roots)
while len(to_visit) > 0:
    curr = first_fulfilled(to_visit, visited, nodes_to_parents)
    visited.add(curr)
    order.append(curr)
    if curr not in nodes_to_children:
        continue
    for child in nodes_to_children[curr]:
        if child not in visited and child not in set(to_visit):
            to_visit.append(child)
    to_visit = sorted(to_visit)

print(''.join(order))
