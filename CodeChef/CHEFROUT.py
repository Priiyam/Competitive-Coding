for i in xrange(input()):
    x = raw_input()
    ln , ans = len(x), 'yes'
    for i in xrange(ln-1):
        if x[i] > x[i+1]:
            ans='no'
            break
    print ans
