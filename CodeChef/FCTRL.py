import math

def chk(x, cnt):
    while x:
        y=x
        while y%5 == 0:
            y/=5
            cnt+=1
        x-=1
    return cnt

n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    cnt = 0
    z = chk(x, cnt)
    print z
