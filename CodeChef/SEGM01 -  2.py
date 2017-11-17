for _ in xrange(int(raw_input())):
    N = raw_input().strip("0")
    if N.count("0")==0 and len(N)>0:
        print "YES"
    else:
        print "NO"
