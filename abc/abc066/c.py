n = int(input())
a = list(map(int,input().split()))

a.sort()

if a[0] == 0:
    ans = True
    for i in range(n):
        if a[i] != ((i+1)//2)*2:
            ans = False
            break
    if ans:
        print(2**(n//2) % (10**9+7))
    else:
        print(0)
else:
    ans = True
    for i in range(n):
        if a[i] != (i//2)*2+1:
            ans = False
            break
    if ans:
        print(2**(n//2) % (10**9+7))
    else:
        print(0)
