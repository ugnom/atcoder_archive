(n,m) = map(int, input().split())
abss = []
for i in range(n):
    (a,b) = map(int, input().split())
    abss.append((a,b))

abss.sort()
sum = 0
for (a,b) in abss:
    if m > b:
        sum = sum + a*b
        m = m-b
    else:
        sum = sum + a*m
        break

print(sum)
