
def search(i, visited, ns) :
    visited[i] = True
    for next in ns[i]:
        if visited[next] == False:
            search(next, visited, ns)


def dfs(ns):
    visited = [False] * len(ns)
    for i in range(len(ns)):
        search(i, visited, ns)

def main();
    (n,v) = map(int,input().split())
    ns = [[] for _ in range(n)]
    for _ in range(v):
        (st,end) = map(int,input().split())
        ns[st-1].append(end - 1)
        ns[end-1].append(st-1)
    dfs(ns)

if __name__ == '__main__':
    main()
