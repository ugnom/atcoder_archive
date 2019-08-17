words = lambda t : list(map(t, input().split()))
n,k = words(int)

if k % 2 == 1:
    print((n // k)**3)
else:
    print((n//k)**3 + (n//(k//2)-(n//k))**3)
