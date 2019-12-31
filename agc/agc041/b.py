words = lambda t : list(map(t, input().split()))
n,m,v,p = words(int)
a = words(int)

a.sort()
ans = p-1
end = n-p+1
loopend = n-v+1
sm = sum(a[0:end])
needed = (v - (p-1)) * m
#print(a)
for i in range(end):
    sm -= a[i]
    needed -= m
    if a[i] + m < a[end-1]:
        continue
    max_score = (a[i] + m) * (end-i-1) - sm
    #print(a[i]+m, end-i-1, sm)
    #print(max_score, needed)
    if needed <= max_score:
        ans = n-i
        break
print(ans)
