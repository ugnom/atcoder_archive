from functools import reduce

words = lambda t : list(map(t, input().split()))
n = int(input())
xs = words(int)

ys = []
k = 0
for x in xs:
    y = list(reversed(bin(x)))[:-2]
    ys.append(y)
    k = max(k, len(y))

def calc2(ans, i):
    def calc (x,y):
        if i < len(y) and y[i] == "1":
            return x+1
        else:
            return x
    x1 = reduce(calc,ys,0)
    #print(x1,x0)
    ans += x1 * (len(ys)-x1) * (2**(i))
    ans %= 10**9 + 7
    return ans
ans = reduce(calc2, range(k), 0)
print(ans)
