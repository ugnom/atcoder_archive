words = lambda t : list(map(t, input().split()))
n = int(input())
xs = words(int)

s_xs = sorted(xs)
ans = False
if s_xs == xs:
    ans = True
else:
    for i in range(n-1):
        for j in range(i,n):
            f_xs = xs.copy()
            tmp = f_xs[i]
            f_xs[i] = f_xs[j]
            f_xs[j] = tmp
            if s_xs == f_xs:
                ans = True
                break
        if ans == True:
            break
if ans == True:
    print("YES")
else:
    print("NO")
