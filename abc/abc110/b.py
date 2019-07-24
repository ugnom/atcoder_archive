words = lambda t : list(map(t, input().split()))
n,m,x,y = words(int)
xs = words(int)
ys = words(int)

x_max = max(xs)
y_min = min(ys)

if x_max < y_min and x_max < y and y_min > x :
    print("No War")
else:
    print("War")
