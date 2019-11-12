words = lambda t : list(map(t, input().split()))
n,m = words(int)
xs = []
for i in range(m):
    a,b,c = words(int)
    xs.append((b,a,c))

sxs = reversed(sorted(xs))

ans = [-1] * n
ans[-1] = 0
#print(sxs)
for b,a,c in sxs:
    #print(ans, a,b,c)
    if ans[b-1] == -1:
        #print("con")
        continue
    for i in range(a-1,b-1):
        if ans[i] != -1 and ans[i] <= ans[b-1] + c:
            break
        ans[i] = ans[b-1] + c

print(ans[0])
