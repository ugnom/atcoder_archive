words = lambda t : list(map(t, input().split()))
n = int(input())
xs = words(int)

xortill = [0] * n
xortill[0] = xs[0]
for i in range(1,n):
    xortill[i] = xs[i] ^ xortill[i-1]

print(xortill)

for i in range(2**20+1):
    for i in range()
