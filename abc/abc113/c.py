(n,m) = map(int, input().split())
pys = []
for i in range(m):
    (a,b) = map(int, input().split())
    pys.append((a,b,i))

pys.sort()
ans = []
cur = -1
j = 0
for (p,y,i) in pys:
    if cur != p:
        j = 1
        cur = p
    #print(p,y,i,j)
    ans.append((i,"{:0=6}".format(p) + "{:0=6}".format(j)))
    j = j + 1

ans.sort()
for (i, a) in ans:
    print(a)
