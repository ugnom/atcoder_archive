words = lambda t : list(map(t, input().split()))
a,b = words(int)

def gcd(x,y):
    while not y == 0:
        tmp = y
        y = x%y
        x = tmp
    return x

def lcm(x,y):
    return (x * y) // gcd(x,y)

print(lcm(a,b))
