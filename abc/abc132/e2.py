import sys

sys.setrecursionlimit(1000000)

words = lambda t : list(map(t, input().split()))


def dfs(ns,s,t):
    n_steps = [-1] * len(ns)
    def search(i, step):
        #print(i, step, n_steps)
        if n_steps[i] == -1 or n_steps[i] > step
            n_steps[i] = step
        if i == t:
            return
        for next in ns[i]:
            cand = search(next, step+1)
    search(s, 0)
    if n_steps[0][t] == -1:
        print(-1)
    else:
        print(n_steps[0][t] // 3)

def main():
    n,v = words(int)
    ns = [[] for _ in range(n*3)]
    for _ in range(v):
        (st,end) = map(int,input().split())
        ns[st-1].append((end - 1)*2)
        ns[(st-1)*2].append((end-1)*3)
        ns[(st-1)*3].append((end-1))
    s,t = words(int)
    dfs(ns,s-1,t-1)

if __name__ == '__main__':
    main()
