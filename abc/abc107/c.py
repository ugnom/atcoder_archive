words = lambda t : list(map(t, input().split()))
n,k = words(int)
a = words(int)
ans = 10 ** 9 
for i in range(n-k+1):
    l = a[i]
    r = a[i+k-1]
    #print(l,r, ans)
    if l < 0 and r <= 0:
        ans = min(ans, abs(l))
    elif l < 0 and r > 0:
        ans = min(ans, min(abs(l), r) * 2 + max(abs(l), r))
    else: # l >= 0 and r > 0
        ans = min(ans, r)

print(ans)
