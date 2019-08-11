words = lambda t : list(map(t, input().split()))
n,m,p = words(int)

def bellman_ford(edges, numv, stt):
  #グラフの初期化
  inf = float("inf")
  dist = [inf for i in range(numv)]
  dist[stt - 1] = 0

  for i in range(numv):
    for (f,t,c) in edges:
      if dist[t-1] > dist[f-1] + c:
        dist[t-1] = dist[f-1] + c
        if i==numv-1:
          print(dist)
          return (-1, dist)

  return (0, dist)


edges = []
for i in range(m):
    a,b,c = words(int)
    edges.append((a,b,-c+p))

ans = bellman_ford(edges, n, 1)
if ans[0] == -1 and ans[1][n-1] == float("inf"):
    print(-1)
else:
    print(max(0,-ans[1][n-1]))
