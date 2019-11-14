a,b,q = list(map(int, input().split()))

s = [0]*a
t = [0]*b
x = [0]*q
for i in range(a):
    s[i] = int(input())
for i in range(b):
    t[i] = int(input())
for i in range(q):
    x[i] = int(input())
s.sort()
t.sort()

INT_MAX = 10**11

#print(s)
#print(t)
import bisect
def func(xi):
    i = bisect.bisect_left(s,xi)
    s_right = INT_MAX
    if i < len(s):
        s_right = s[i] - xi
    s_left = INT_MAX
    if i != 0:
        s_left = xi - s[i-1]
    j = bisect.bisect_left(t,xi)
    t_right = INT_MAX
    if j < len(t):
        t_right = t[j] - xi
    t_left = INT_MAX
    if j != 0:
        t_left = xi - t[j-1]
    #print(i,j,xi)
    #print(s_left,s_right,t_left,t_right)
    return min(max(s_right,t_right), max(s_left,t_left), min(s_left,t_right)*2+max(s_left,t_right), min(s_right,t_left)*2+max(s_right,t_left))

ans = map(func, x)
print("\n".join(map(str,ans)))
