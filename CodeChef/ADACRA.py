n = int(raw_input())
for i in xrange(n):
    inp = raw_input()
    cnt=0
    ran = 'a'
    for j in inp:
        if j!=ran:
            cnt+=1
        ran = j
    print cnt/2
