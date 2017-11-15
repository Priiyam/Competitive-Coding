for i in xrange(input()):
    x = input()
    l1 = map(int,raw_input().split())
    j=-1
    ans="yes"
    if len(l1)%2==0:
        ans="no"
    else:
        for i in range((len(l1)/2)+1):
            if not(l1[i] == l1[j-i]) or not(l1[i]==i+1):
                ans="no"
                break
    print ans
