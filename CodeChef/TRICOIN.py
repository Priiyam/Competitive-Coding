n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    sum,h = 0,0
    for j in range(1,x+1):
        sum+=j
        if sum > x:
            break
        h += 1
    print h