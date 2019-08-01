words = lambda t : list(map(t, input().split()))
a,b = words(int)

if a % 2 != 0 and b % 2 != 0:
    print("Yes")
else:
    print("No")
