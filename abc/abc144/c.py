words = lambda t : list(map(t, input().split()))
n = int(input())

ans = n-1
i = 1
while i*i <= n:
    if n % i == 0:
        #print(n,i, ans)
        ans = min(ans, i + n//i - 2)
    i+=1
print(ans)
