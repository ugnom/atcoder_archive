words = lambda t : list(map(t, input().split()))
n,d = words(int)

dd = 2*d + 1
if n % dd == 0:
    print(n//dd)
else:
    print(n//dd+1)
