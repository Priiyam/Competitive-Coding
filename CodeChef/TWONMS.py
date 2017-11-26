n = int(raw_input())
for i in range(n):
    a, b, k = map(int, raw_input().split())
    if k%2==0:
        print max(a, b)/min(a, b)
    else:
        print max(a*2, b)/min(a*2, b)