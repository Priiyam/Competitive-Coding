for i in xrange(input()):
    x = input()
    l1 = "".join(raw_input().split())
    l1 = l1.lstrip('1')
    sum=0
    sum+=(l1.count('0')*1100)
    sum+=(l1.count('1')*100)
    print sum