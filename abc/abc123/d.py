x,y,z,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = list(reversed(sorted(a)))
b = list(reversed(sorted(b)))
c = list(reversed(sorted(c)))

abc = []
for p in range(x):
    for q in range(y):
        if (p+1) * (q+1) > k:
            break
        for r in range(z):
            if (p+1) * (q+1) * (r+1) > k:
                break
            abc.append(a[p]+ b[q] + c[r])

abc = list(reversed(sorted(abc)))

for i in range(k):
    print(abc[i])
