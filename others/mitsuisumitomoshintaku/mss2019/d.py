words = lambda t : list(map(t, input().split()))
n = int(input())
a = input()

d = {}
for i in range(n-2):
    nums = [0]*10
    for j in range(i+2,n):
        nums[int(a[j-1])] += 1
        #print(i,j, nums)
        for k in range(10):
            if nums[k] > 0:
                d[int(a[i])*100 + k*10 + int(a[j])] = 1
        #print(d)

print(len(d))
