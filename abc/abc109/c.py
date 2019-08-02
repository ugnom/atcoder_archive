words = lambda t : list(map(t, input().split()))
n,x = words(int)
xs = words(int)

def gcd(x,y):
    while not y == 0:
        tmp = y
        y = x%y
        x = tmp
    return x

ys = list(map(lambda y: abs(y-x), xs))
g = ys[0]
for y in ys:
    g = gcd(g,y)

print(g)
