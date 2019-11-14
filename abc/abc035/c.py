n,q = list(map(int,input().split()))

lr = []
for i in range(q):
    l,r = list(map(int,input().split()))
    lr.append((l,r))

a = [0]*(n+1)
for l,r in lr:
    #print("".join(map(str,a)))
    a[l-1] += 1
    a[r] -= 1
#print("".join(map(str,a)))

b = [0] * n
b[0] = a[0] % 2
for i in range(1,n):
    b[i] = (b[i-1] + a[i]) % 2

print("".join(map(str,b)))
