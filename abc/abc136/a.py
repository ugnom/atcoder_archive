words = lambda t : list(map(t, input().split()))
a,b,c = words(int)

print(max(0, c - (a - b)))
