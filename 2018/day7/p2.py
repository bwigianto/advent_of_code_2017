import sys

n = 5
def roots(nodes_to_parents):
    return set(node for node, parents in nodes_to_parents.items() if not parents)

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
        nodes_to_work[letter] = ord(letter) - 4
    if child_letter not in nodes_to_work:
        nodes_to_work[child_letter] = ord(child_letter) - 4

def fulfilled(node, finished, nodes_to_parents):
    return all(x in finished for x in nodes_to_parents[node])

def ready(curr_nodes, to_visit, finished, nodes_to_parents):
    i = 0
    while len(curr_nodes) < n and i < len(to_visit):
        if fulfilled(to_visit[i], finished, nodes_to_parents):
            curr_nodes.append(to_visit.pop(i))
        else:
            i += 1

def work(nodes, nodes_to_work):
    dt = min(nodes_to_work[node] for node in nodes)
    for node in nodes:
        nodes_to_work[node] -= dt
    return dt

roots = roots(nodes_to_parents)
to_visit = sorted(roots)
order = []
finished = set()
t = 0
curr_nodes = []
while len(to_visit) > 0:
    ready(curr_nodes, to_visit, finished, nodes_to_parents)
    t += work(curr_nodes, nodes_to_work)
    i = 0
    while i < len(curr_nodes):
        node = curr_nodes[i]
        if nodes_to_work[node] == 0:
            finished.add(node)
            order.append(node)
            curr_nodes.pop(i)
            i -= 1
            for child in nodes_to_children[node]:
                if child not in finished and child not in set(to_visit):
                    to_visit.append(child)
        i += 1
    to_visit = sorted(to_visit)

print(t)
