for i in range(input()):
    x = raw_input()
    cnt=x.count('=')
    x = x.replace('=','')
    start = x[0]
    for i in x:
        if i==start:
            start = i
        else:
            start = i
            cnt += 1
    print cnt