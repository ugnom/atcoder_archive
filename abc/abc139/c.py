words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

cur_max = 0
cur = 0
for i in range(1,n):
    #(i, a[i], a[i-1])
    if a[i] <= a[i-1]:
        cur += 1
    else:
        cur_max = max(cur_max, cur)
        cur = 0

cur_max = max(cur_max, cur)
print(cur_max)
