for t in xrange(int(raw_input())):
    n = int(raw_input())
    st = raw_input().strip()
    a = st
    for i in range(n):
        c = st[i]
        x = st[:i]+st[i+1:]
        for j in range(n):
            temp = x[:j]+c+x[j:]
            a = min(a, temp)
    print a