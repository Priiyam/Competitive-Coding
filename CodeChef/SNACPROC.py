r = int(raw_input())
for i in range(r):
    l = int(raw_input())
    x = raw_input().upper();
    if len(x)==l:
        for i in list(set(x)):
            if i not in list(set(x)):
                print 'Invalid'
                break
        cond=1
        xlist = filter(lambda a: a!= '.', list(x))
        for j in range(0,len(xlist)-1,2):
            if (len(xlist) % 2) == 1:
                print 'Invalid'
                cond=0
                break
            if not((xlist[j]=='H') and (xlist[j+1]=='T')):
                print 'Invalid'
                cond=0
                break
        if (cond):
            print 'Valid'
    else:
        print 'Invalid'

