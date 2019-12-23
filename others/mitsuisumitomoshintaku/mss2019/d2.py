words = lambda t : list(map(t, input().split()))
n = int(input())
a = input()

d = {}
r_nums = [0] * 10
for i in range(1,n):
    r_nums[int(a[i])] += 1
l_nums = [0] * 10

for i in range(1,n-1):
    center = int(a[i])
    r_nums[int(a[i])] -= 1
    l_nums[int(a[i-1])] += 1
    #print(l_nums, center, r_nums)
    for j in range(10):
        for k in range(10):
            if r_nums[j] > 0 and l_nums[k] > 0:
                d[k*100 + center*10 + j] = 1
    #print(d)
print(len(d))
