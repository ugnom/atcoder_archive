words = lambda t : list(map(t, input().split()))
a,b = words(int)

if (a + b) % 2 != 0:
    print("IMPOSSIBLE")
else:
    print((a+b)//2)
