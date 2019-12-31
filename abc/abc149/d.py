words = lambda t : list(map(t, input().split()))
n = int(input())
xs = words(int)


cnt = 1
for i in range(n):
    if xs[i] == cnt:
        cnt += 1
if cnt == 1:
    print(-1)
else:
    print(n-cnt+1)
