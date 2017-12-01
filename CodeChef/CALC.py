for i in range(input()):
    x, y = map(int, raw_input().split())
    z = x/y
    k = x%y
    if k:
        print ((z/2)+1)*((z-(z/2)-1)*(y)+k)
    else:
        print ((z / 2)) * ((z - (z / 2) ) * y) +k