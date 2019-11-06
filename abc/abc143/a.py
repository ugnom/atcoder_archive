words = lambda t : list(map(t, input().split()))
a,b = words(int)

print(max(0, a - 2*b))
