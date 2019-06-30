import sys

sys.setrecursionlimit(1000000)

words = lambda t : list(map(t, input().split()))


def dfs(ns,s,t):
    n_steps = [[-1] * len(ns) for i in range(3)]
    def search(i, step):
        #print(i, step, n_steps)
        if step % 3 == 0 and i == t:
            n_steps[0][i] = step
            return
        j = step % 3
        if n_steps[j][i] == -1 or (n_steps[j][i] > step):
            n_steps[j][i] = step
            for next in ns[i]:
                cand = search(next, step+1)
    search(s, 0)
    if n_steps[0][t] == -1:
        print(-1)
    else:
        print(n_steps[0][t] // 3)

def main():
    n,v = words(int)
    ns = [[] for _ in range(n)]
    for _ in range(v):
        (st,end) = map(int,input().split())
        ns[st-1].append(end - 1)
    s,t = words(int)
    dfs(ns,s-1,t-1)

if __name__ == '__main__':
    main()
