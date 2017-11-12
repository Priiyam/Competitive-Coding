for i in xrange(int(raw_input())):
    x = int(raw_input())
    if x==1:
        print 1
    else:
        for j in range(x):
            print 2*j+1,
        print
