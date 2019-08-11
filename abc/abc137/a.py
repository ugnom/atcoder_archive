words = lambda t : list(map(t, input().split()))
a,b = words(int)
print(max(a+b,a-b,a*b))
