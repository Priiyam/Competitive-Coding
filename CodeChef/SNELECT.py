for i in xrange(int(raw_input())):
    x = raw_input()
    cnt = x.count('m')
    x = x.replace('sm','')
    x = x.replace('ms','')
    if x.count('s') == cnt:
        print "tie"
    elif x.count('s') > cnt:
        print "snakes"
    else:
        print "mongooses"


