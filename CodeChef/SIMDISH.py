for i in xrange(input()):
    l1 = raw_input().split()
    l2 = raw_input().split()
    l1.extend(l2)
    if len(set(l1))<=6:
        print "similar"
    else:
        print "dissimilar"
