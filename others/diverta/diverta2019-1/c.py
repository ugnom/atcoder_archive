words = lambda t : list(map(t, input().split()))
n = int(input())

ab = 0
ba = 0
a = 0
b = 0
for _ in range(n):
    s = input()
    for i in range(len(s)-1):
        #print(i)
        if s[i] == "A" and s[i+1] == "B":
            ab += 1
    if s[0] == "B" and s[-1] == "A":
        ba += 1
    elif s[0] == "B":
        b += 1
    elif s[-1] == "A":
        a += 1

if ba > 0:
    ab += ba-1
    ba = 1
    if a > 0:
        ab += 1
        ba = 0
    elif b > 0:
        ab += 1
        ba = 0
print(ab + min(a,b))
