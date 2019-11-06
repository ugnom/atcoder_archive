words = lambda t : list(map(t, input().split()))
n,k = words(int)
h = words(int)

cnt = 0
for hi in h:
    if hi >= k:
        cnt += 1
print(cnt)
