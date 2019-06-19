(a,b) = map(int, input().split())
xs = []
if a % 2 == 1:
    xs.append(a)
    a = a+1
if b % 2 == 0:
    xs.append(b)
    b = b-1

if (b-a+1)//2 % 2 == 1:
    xs.append(1)
#print(xs)
ans = 0
for x in xs:
    ans = ans ^ x

print(ans)
