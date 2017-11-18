arr = raw_input().split()
x = int(arr[0])
y = float(arr[1])
if (x%5 == 0) and (y-x-0.50>0):
    print("%.2f" % (y-x-0.50))
else:
    print ("%.2f" % y)