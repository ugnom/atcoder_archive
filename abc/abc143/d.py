from bisect import bisect_right

words = lambda t : list(map(t, input().split()))
n = int(input())
k = words(int)
k.sort()

ans = 0
for i in range(n-2):
    for j in range(i,n-1):
        x = bisect_right()
