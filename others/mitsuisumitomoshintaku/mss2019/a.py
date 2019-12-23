words = lambda t : list(map(t, input().split()))
a,b = words(int)
c,d = words(int)

if a != c:
    print(1)
else:
    print(0)
