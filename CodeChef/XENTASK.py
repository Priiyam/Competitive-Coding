for i in xrange(input()):
    x = input()
    l1 = map(int, raw_input().split())
    l2 = map(int, raw_input().split())
    l11,l12,l21,l22 = 0, 0, 0, 0
    for i in range(len(l1)):
        if i%2==0:
            l12+=l1[i]
            l22+=l2[i]
        else:
            l11+=l1[i]
            l21+=l2[i]
    print min(l11+l22, l12+l21)