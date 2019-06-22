words = lambda t : list(map(t, input().split()))
n,k = words(int)

max_m = sum(range(1,n-1))
if k > max_m:
    print(-1)
else:
    g = []
    for i in range(n):
        for j in range(i+1,n):
            g.append((i,j))
    #print(g)
    for i in range(k):
        g.pop(-1)

    print(len(g))
    for a,b in g:
        print(a+1,b+1)
