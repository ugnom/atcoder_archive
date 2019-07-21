words = lambda t : list(map(t, input().split()))
n = int(input())
xs = []
fst = 0
snd = 0
for i in range(n):
    x = int(input())
    xs.append(x)
    if x > fst:
        t = fst
        fst = x
        x = t
    if x > snd:
        snd = x

for a in xs:
    if a == fst:
        print(snd)
    else:
        print(fst)
