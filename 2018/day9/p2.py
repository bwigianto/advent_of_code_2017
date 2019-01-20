#!/usr/bin/python
class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev 

def add(A, i):
    if i % 23 != 0:
        left = A.next
        right = A.next.next
        new = Node(i, right, left)
        left.next = new
        right.prev = new
        return new, 0
    left = A.prev.prev.prev.prev.prev.prev.prev.prev
    removed = A.prev.prev.prev.prev.prev.prev.prev
    right = A.prev.prev.prev.prev.prev.prev
    left.next = right
    right.prev = left
    return right, i + removed.val

def display(A):
    curr = A.next
    out = [A.val]
    while curr.val != A.val:
        out += [curr.val]
        curr = curr.next
    print(out)

def max_score(n, marbles):
    scores = {i : 0 for i in range(n)}
    A = Node(0, None, None)
    A.prev = A
    A.next = A
    
    for i in range(1, marbles + 1):
        A , score = add(A, i)
        scores[i % n] += score
        #display(A)
    return max(scores.values())


#print(max_score(9, 25))
#print(max_score(10, 1618))
#print(max_score(13, 7999))
#print(max_score(17, 1104))
#print(max_score(21, 6111))
#print(max_score(30, 5807))
print(max_score(400, 7186400))

