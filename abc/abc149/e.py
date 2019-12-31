45words = lambda t : list(map(t, input().split()))
n = int(input())

xs = []
for i in range(30):
    xs.append((n // (5**i)) // 2)

#print(xs)
if n % 2 == 0:
    print(sum(xs[1:]))
else:
    print(0)
