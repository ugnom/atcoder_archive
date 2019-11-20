words = lambda t : list(map(t, input().split()))
n = int(input())
xys = []
for i in range(n):
    x,y = words(int)
    xys.append((x,y))

import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

fn = math.factorial(n)
nc2 = math.factorial(n) // (math.factorial(2) * math.factorial(n-2))

ans = 0
for i in range(n-1):
    for j in range(i,n):
        d = distance(xys[i][0], xys[i][1], xys[j][0], xys[j][1])
        ans += d * (fn // nc2)

print(ans*(n-1)/fn)
