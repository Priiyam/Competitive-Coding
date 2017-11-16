import re

n = int(raw_input())
for i in xrange(n):
    inp = raw_input()
    l1 = [m.group(0) for m in re.finditer(r"(\d)\1*", inp)]
    k=0
    for i in l1:
        if i[0]=='1':
            k+=1
            if k>1:
                break
    if k==0 or k>1:
        print 'NO'
    else:
        print 'YES'

