words = lambda t : list(map(t, input().split()))
n = int(input())

vs = [[] for i in range(n)]
for i in range(n-1):
    s,e = words(int)
    vs[s-1].append((e-1,i))

import queue
q = queue.Queue()
q.put(0)
color = [0] * (n-1)
color_par = [0] * (n)
color_par[0] = -1
while not q.empty():
    v = q.get()
    cur_c = 1
    for (c,i) in vs[v]:
        if color_par[v] == cur_c:
            cur_c +=1
        color[i] = cur_c
        color_par[c] = cur_c
        cur_c += 1
        q.put(c)

print(max(color))
for i in range(n-1):
    print(color[i])
