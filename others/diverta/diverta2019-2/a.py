words = lambda t : list(map(t, input().split()))
n,k = words(int)

if k == 1:
    print(0)
else:
    print(n-k)
