n = int(raw_input())
for i in xrange(n):
    N = int(raw_input())
    l1 = map(int, raw_input().split())
    a = l1.count(0)
    b = l1.count(1)
    c = l1.count(-1)
    sm = N-a-b-c
    if sm>1:
        print 'no'
    elif sm>0 and c>0:
        print 'no'
    elif b==0 and c>1:
        print 'no'
    else:
        print 'yes'
