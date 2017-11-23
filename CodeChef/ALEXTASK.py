for i in xrange(input()):
    x = input()
    l1 = map(int, raw_input().split())
    c=l1
    a = map(lambda x:x*2, l1)
    for i in a:
        c.append(i)
    b = set(c)
    cond=1
    while (cond):
        if len(c)!=len(b):
            for j in b:
                if c.count(j)==2:
                    print j
                    cond=0
                    break
        else:
            a = map(lambda x: x * (2**(cond)), l1)
            for i in a:
                c.append(i)
            b = set(c)


