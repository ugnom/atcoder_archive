words = lambda t : list(map(t, input().split()))

n = int(input())
xs = []
for i in range(n):
    a,b = words(int)
    xs.append((b,a))

xs.sort()

ttl = 0
succeed = True
for b,a in xs:
    ttl += a
    if ttl > b:
        succeed = False
        break

if succeed:
    print("Yes")
else:
    print("No")
