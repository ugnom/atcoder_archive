import sys
sys.setrecursionlimit(10**6 + 1000)

words = lambda t : list(map(t, input().split()))
n = int(input())
s = input()

a = [0] * len(s)
for i in range(len(s)):
    if s[i] == "B":
        a[i] = 1
    else:
        a[i] = 0

l = 0
r = len(a)-1

def recur(l,r,cur_n,k):
    #print(l,r,cur_n,k)
    if l >= r:
        return 0
    if l+1 == r:
        if a[l] == a[r] and a[l] == k:
            return 1
        else:
            return 0
    ret = 0
    if a[l] == a[l+1] and a[l] == k:
        ret += recur(l+2,r, cur_n-1,k)
        ret %= (10**9 + 7)
    if a[r] == a[r-1] and a[r] == k:
        ret += recur(l,r-2,cur_n-1,k)
        ret %= (10**9 + 7)
    if a[l] == a[r] and a[l]== k:
        ret += recur(l+1,r-1,cur_n-1,(k+1)%2)
        ret %= (10**9 + 7)
    #print(ret)
    return cur_n * (cur_n - 1) * ret % (10**9 + 7)

print(recur(l,r,n,1))
