words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
b = [0] * n

for i in reversed(range(n)):
    t = i+1
    if t*2 > n:
        b[i] = a[i]
    else:
        #print(i, b[i], i*2+1, a[i*2+1])
        b[i] = a[i*2+1]
        j = i + (t*2)
        #print(j,b[i])
        #print(b)
        while j < n:
            b[i] += b[j]
            #print(j, b[j], b[i])
            j += t*2
        b[i] = b[i] % 2
        #print(a[i], b[i])
        if b[i] == a[i]:
            b[i] = 0
        else:
            b[i] = 1

#print(b)
ans = []
for i in range(len(b)):
    if b[i] == 1:
        ans.append(str(i+1))
print(len(ans))
if len(ans) > 0:
    print(" ".join(ans))
