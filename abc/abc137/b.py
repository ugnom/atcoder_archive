words = lambda t : list(map(t, input().split()))
k,x = words(int)

ans = []
for i in range(max(-2000000, x-k+1), min(2000001, x+k)):
    ans.append(str(i))

print(" ".join(ans))
