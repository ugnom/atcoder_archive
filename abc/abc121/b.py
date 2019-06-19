(n,m,c) = map(int, input().split())
bs = list(map(int, input().split()))
cnt = 0
for _ in range(n):
    #print(cnt)
    ass = list(map(int, input().split()))
    #print(ass)
    sum = 0
    for (a,b) in zip(ass,bs):
        sum = sum + a*b
    #print(sum)
    if sum + c > 0:
        cnt = cnt + 1

print(cnt)
