words = lambda t : list(map(t, input().split()))
n = int(input())
s = input()

if n % 2 != 0:
    print("No")
else:
    ans = True
    for i in range(n//2):
        #print(i,n//2 +1, s[i], s[n//2+i])
        if s[i] != s[n//2 + i]:
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")
