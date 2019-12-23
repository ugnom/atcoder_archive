words = lambda t : list(map(t, input().split()))

n,u,v = words(int)
u -= 1
v -= 1

edges = [[] for i in range(n)]
for i in range(n-1):
    f,t = words(int)
    edges[f-1].append(t-1)
    edges[t-1].append(f-1)

from queue import Queue
def bfs1(edges,stt):
    dist = [-1] * n
    q = Queue()
    q.put(stt)
    dist[stt] = 0
    #print(q)
    while not q.empty():
        v = q.get()
        #print(v)
        for c in edges[v]:
            #print("es", c)
            if dist[c] == -1:
                dist[c] = dist[v]+1
                q.put(c)
    return dist

dist_v = bfs1(edges, v)
dist_u = bfs1(edges, u)
#print(u,v)
#print(edges)
#print(dist_v)
#print(dist_u)

ans = 0
for i in range(n):
    if dist_v[i] > dist_u[i]:
        ans = max(ans,dist_v[i])

print(max(ans-1,0))
