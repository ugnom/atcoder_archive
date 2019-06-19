words = lambda t : list(map(t, input().split()))
w,h,x,y = words(int)
if x == w/2 and y == h/2:
    print((w*h)/2, 1)
else:
    print((w*h)/2, 0)
