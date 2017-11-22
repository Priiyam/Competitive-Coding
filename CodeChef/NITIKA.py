for i in xrange(input()):
    x = raw_input().lower().split()
    ln = len(x)
    if (ln==1):
        print x[0].capitalize()
    elif (ln==2):
        print (x[0])[0].capitalize() + '. ' + x[1].capitalize()
    else:
        print (x[0])[0].capitalize() + '. ' + (x[1])[0].capitalize() + '. ' + x[2].capitalize()
