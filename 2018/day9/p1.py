#!/usr/bin/python

def add(A, i, curr):
    if i == 0:
        A.append(0)
        return 0, 0
    if i % 23 == 0:
        to_remove = (curr - 7) % len(A)
        score = i + A.pop(to_remove)
        return to_remove % len(A), score
    if curr == len(A) - 1:
        next_curr = 1
    elif curr == len(A) - 2:
        next_curr = len(A)
    else:
        next_curr = (curr + 2) % (len(A) + 1)
    A.insert(next_curr, i)
    return next_curr, 0
    

def max_score(n, marbles):
    scores = {i : 0 for i in range(n)}
    A = []
    curr = None
    for i in range(marbles + 1):
        curr, score = add(A, i, curr)
        scores[i % n] += score
        #print(A, curr)
    return max(scores.values())


#print(max_score(10, 1618))
#print(max_score(13, 7999))
#print(max_score(17, 1104))
#print(max_score(21, 6111))
#print(max_score(30, 5807))
print(max_score(400, 7186400))

