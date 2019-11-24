n = int(input())

red = []
for i in range(n):
    a,b = list(map(int,input().split()))
    red.append((a,b))
blue = []
for i in range(n):
    c,d + list(map(int,input().split()))

vs = [[] for i in range(n)]
vxs = [[] for i in range(n+2)]
for i in range(n):    
    vxs[n].append(i)
    vxs[i].append(n+1)
for i, (a,b) in enumerate(red):
    for j, (c,d) in enumerate(blue):
        if a < c and b < d:
            vs[i].append(j)
