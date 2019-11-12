words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

mv = max(a)

xs = [0] * (mv+1)
for y in a:
    xs[y] += 1

#print(xs)

if xs[0] > 1:
    print(0)
elif a[0] != 0:
    print(0)
else:
    ans = 1
    for i in range(len(xs)-1):
        ans *= xs[i] ** xs[i+1]
        ans %= 998244353

    print(ans)
