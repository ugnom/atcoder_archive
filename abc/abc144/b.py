words = lambda t : list(map(t, input().split()))
n = int(input())

ans = False
for i in range(1,10):
    for j in range(1,10):
        if n == i*j:
            ans = True

if ans:
    print("Yes")
else:
    print("No")
