words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
ab = []
for i in range(1,n+1):
    ab.append((a[i-1],i))

ab.sort()
b = []
for (a,i) in ab:
    b.append(i)

#print(ab)
print(" ".join(map(str,b)))
