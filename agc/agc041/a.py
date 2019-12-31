words = lambda t : list(map(t, input().split()))

n,a,b = words(int)
if (a - b) % 2 == 0:
    print(abs(a-b) // 2)
else:
    print(min((a+b-1)//2, ((n-a) + (n-b) + 1)//2))
