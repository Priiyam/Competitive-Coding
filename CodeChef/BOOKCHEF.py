N, M = map(int, raw_input().split())
l1 = (raw_input().split())
l2, l3 = [], []
for i in xrange(M):
    f,p,s = raw_input().split()
    if f in l1:
        l2.append({int(p):s})
    else:
        l3.append({int(p):s})
l2.sort(reverse=True)
l3.sort(reverse=True)
for i in l2:
    for j in i:
        print i[j]
for i in l3:
    for j in i:
        print i[j]
