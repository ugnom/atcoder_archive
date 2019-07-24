words = lambda t : list(map(t, input().split()))
xs = words(int)
xs = list(reversed(sorted(xs)))
print(xs[0]*10 + xs[1] + xs[2])
