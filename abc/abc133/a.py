words = lambda t : list(map(t, input().split()))
n,a,b = words(int)

print(min(n*a, b))
