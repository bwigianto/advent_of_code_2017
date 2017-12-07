import sys


names = {}
for line in sys.stdin:
   parts = line.strip().split('->') 
   name = parts[0].split(' ')[0].strip()
   weight = int(parts[0].strip().split(' ')[1].strip().replace('(','').replace(')',''))
   if len(parts) == 1:
       names[name] = [weight, [], None]
   elif len(parts) == 2:
       children = [x.strip() for x in parts[1].split(', ')]
       names[name] = [weight, children, None]
for name, val in names.iteritems():
    for child in val[1]:
        names[child][2] = name

for name, val in names.iteritems():
    if val[2] == None:
        print name

def weight(name):
    if len(names[name][1]) == 0:
        return names[name][0]
    return names[name][0] + sum(weight(child) for child in names[name][1])

def weights(name):
    return [(child, weight(child)) for child in names[name][1]] 

def weird(child_weights):
    ct1 = 0
    name1 = None
    ct2 = 0
    name2 = None
    if len(child_weights) > 2:
        for cw in child_weights:
            if name1 == None or cw[0] == name1:
                name1 = cw[0]
                ct1 += 1
            else:
                name2 = cw[0]
                ct2 += 1
    if ct1 == 1:
        return name1
    return name2
#top = 'cqmvs'
#prev = None
#curr = top
#while prev != curr:
#    print curr
#    wts = weights(curr)
#    print wts
#    prev = curr
#    curr = weird(wts)
#[('zumdwwu', 99), ('lvazjz', 99), ('qhiav', 99)]
print names['zumdwwu'], weights('zumdwwu')
print names['lvazjz'], weights('lvazjz')
print names['qhiav'], weights('qhiav')
print names['vmttcwe']

