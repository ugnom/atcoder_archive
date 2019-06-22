words = lambda t : list(map(t, input().split()))
n,l = words(int)

if l > 0:
    print(sum(range(l+1,l+n)))
elif l <= 0 and n > abs(l):
    ans = 0
    for i in range(l,l+n):
        ans += i
    print(ans)
else:
    #print("else")
    print(sum(range(l,l+n-1)))
