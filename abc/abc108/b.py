words = lambda t : list(map(t, input().split()))
x1,y1,x2,y2 = words(int)

x3 = x2 + y1 - y2
y3 = y2 + x2 - x1

x4 = x3 + x1 - x2
y4 = y3 + y1 - y2

print(x3,y3,x4,y4)
