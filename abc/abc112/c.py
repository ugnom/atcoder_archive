n = int(input())
xs = []
zs = []
for i in range(n):
    x,y,h = list(map(int,input().split()))
    if h == 0:
        zs.append((x,y,h))
    else:
        xs.append((x,y,h))

for i in range(101):
    for j in range(101):
        top = -1
        ans = True
        for x,y,h in xs:
            if top == -1:
                top = h + abs(x-i) + abs(y-j)
            if top != h + abs(x-i) + abs(y-j):
                ans = False
                break
        for x,y,h in zs:
            if top - abs(x-i) - abs(y-j) > 0:
                ans = False
                break
        if ans:
            break
    if ans:
        break
if top == -1:
    top = 1
print(i,j,top)
