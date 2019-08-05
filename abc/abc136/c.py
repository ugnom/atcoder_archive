words = lambda t : list(map(t, input().split()))
n = int(input())
h = words(int)

h[0] -= 1
ans = True
for i in range(1,n):
    if h[i-1] > h[i]:
        ans = False
        break
    elif h[i-1] == h[i]:
        continue
    else: # h[i-1] < h[i]
        h[i] -= 1
if ans:
    print("Yes")
else:
    print("No")
