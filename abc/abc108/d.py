words = lambda t : list(map(t, input().split()))
l = int(input())

import math
p = math.log(l,2)
r = l - 2**p

ans = []
for i in p:
    ans.append((i+1,i+2,0))
    ans.append((i+1,i+2,1))
