words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)
b = words(int)

ba = list(zip(b,a))
ba.sort()

sa = sorted(a)
sb = sorted(b)
ans = True
for sai,sbi in zip(sa,sb):
    if sai > sbi:
        ans = False
        break
if not ans:
    print("No")
    exit()

rsb = reversed(sb)
j = -1
for ai in reversed(sa):
    
