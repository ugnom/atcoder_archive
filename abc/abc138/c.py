words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

a.sort()

cur = a[0]
for i in range(1,len(a)):
    cur = (cur + a[i]) / 2

print(cur)
