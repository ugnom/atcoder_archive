words = lambda t : list(map(t, input().split()))
n,k = words(int)
a = words(int)

ttl = 0
ans = 0
j = 0
for i in range(n):
    while ttl < k and j < n:
        #print(i,":",a[i],j,":", a[j],ttl,ans)
        ttl += a[j]
        j+=1
    if ttl >= k:
        ans += n-j+1
    ttl -= a[i]
print(ans)
