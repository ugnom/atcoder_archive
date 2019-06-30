words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
a.sort()

print(a[n//2] - a[n//2-1])
    
