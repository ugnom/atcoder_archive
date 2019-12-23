


def dfs(edges, visited, cur, end):
    if visited[cur]:
        return (False,[])
    print(cur,end)
    if cur == end:
        return (True,[cur])
    visited[cur] = True
    path = []
    for next in edges[cur]:
        path = dfs(edges, visited, next, end)
        print(cur,next,path)
        if path[0]:
            path[1].append(cur)
            break
    return path

n,g,e = list(map(int,input().split()))
gs = list(map(int,input().split()))
edges = [[] for i in range(n+1)]
for i in range(e):
    a,b = list(map(int,input().split()))
    edges[a].append(b)
    edges[b].append(a)

for gi in gs:
    edges[gi].append(n)

visited = [False] * (n+1)

path = dfs(edges, visited, 0, n)
print(list(reversed(path[1])))
