def mfibo(a, b, k, cnt):
    if cnt != k:
        cnt+=1
        return mfibo(b,b-a, k, cnt)
    else:
        return b % 1000000007

n = int(raw_input())
for i in xrange(n):
    a, b, k = map(int, raw_input().split())
    cnt=2
    print mfibo(a,b,k,cnt)
