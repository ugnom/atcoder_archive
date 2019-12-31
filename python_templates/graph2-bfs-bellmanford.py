words = lambda t : list(map(t, input().split()))
n,m,p = words(int)

w_edges = []
f_edges = [[] for _ in range(n)]
b_edges = [[] for _ in range(n)]

for i in range(m):
    a,b,c = words(int)
    w_edges.append((a-1,b-1,c))
    f_edges[a-1].append((b-1))
    b_edges[b-1].append((a-1))

from queue import Queue
def bfs(edges,stt):
    visited = [False] * n
    q = Queue()
    q.put(stt)
    visited[stt] = True
    while not q.empty():
        v = q.get()
        for c in edges[v]:
            if not visited[c]:
                visited[c] = True
                q.put(c)
    return visited

f_visited = bfs(f_edges, 0)
b_visited = bfs(b_edges, n-1)

edges = []
for a,b,c in w_edges:
    if f_visited[a] and b_visited[a] and f_visited[b] and b_visited[b]:
        edges.append((a,b,p-c))

def bellman_ford(edges, num_v, stt):
    inf = float('inf')
    dist = [inf]*num_v
    dist[stt] = 0
    for i in range(num_v+1):
        for a,b,c in edges:
            prev = dist[b]
            dist[b] = min(dist[b], dist[a]+c)
            if i == num_v and prev != dist[b]:
                return -1
    return dist

d = bellman_ford(edges, n, 0)
if d == -1:
    print(-1)
else:
    print(max(0,-d[n-1]))
