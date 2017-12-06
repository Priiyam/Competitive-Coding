def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

t = int(raw_input())
for i in range(0, t):
    n = int(raw_input())
    l1 = map(int, raw_input().split())
    l1 = qsort(l1)
    print l1[0]+l1[1]

