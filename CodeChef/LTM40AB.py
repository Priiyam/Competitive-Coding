for i in xrange(input()):
    a, b, c, d = map(int, raw_input().split())
    sum=0
    for i in xrange(a, b+1):
        sum = sum + (d-i)
    if sum <= 0:
        print 0
    else :
        print sum
