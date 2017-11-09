import sys

def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)/2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i=j=0
    for k in range(first, last+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

L=[]
n = int(raw_input())
for i in range(n):
    a,b = map(int, raw_input().split())
    L2 = map (int, raw_input().split())
    if len(L2) == a:
        merge_sort(L2)
        N1 = min(  sum(L2[ : b] ), sum(L2[ b : ] ) )
        N2 = min(  sum(L2[ : a-b] ), sum(L2[ a-b : ] ) )
        print sum(L2) - 2*min(N1, N2)


