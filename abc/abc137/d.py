from collections import deque
import heapq
words = lambda t : list(map(t, input().split()))
n,m = words(int)
ab = []
max_a = 0
for i in range(n):
    a,b = words(int)
    ab.append((b,a))
    max_a = max(a, max_a)

ab.sort()
ab = list(map(lambda ba: (ba[1],ba[0]), ab))
moto = {}

for a,b in ab:
    if a not in moto:
        moto[a] = deque()
    moto[a].append(b)

#print(moto)

h = []
ans = 0
for a in range(m+1):
    #print(a)
    if a in moto:
        #print(moto[a])
        if len(moto[a]) > 0:
            b = moto[a].pop()
            heapq.heappush(h,(-b,a))
    #print(h)
    if len(h) > 0:
        mb,na = heapq.heappop(h)
        if na in moto:
            if len(moto[na]) > 0:
                nb = moto[na].pop()
                heapq.heappush(h,(-nb, na))
        ans += -mb
print(ans)
