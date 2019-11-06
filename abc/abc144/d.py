import math
words = lambda t : list(map(t, input().split()))
a,b,x = words(int)

k = x / (a*a)
if k == b:
    print(0)
elif k*2 == b:
    print(45)
elif k*2 < b:
    print(90 - math.degrees(math.atan(2*x/(a*b*b))))
else:
    p = ((a*b)- (x/a)) / (a/2)
    print(90 - math.degrees(math.atan(a/p)))
