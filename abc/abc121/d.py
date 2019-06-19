(a,b) = map(int, input().split())
bina = bin(a)
bina = bina[2:]
binb = bin(b)
binb = binb[2:]

bina = bina[::-1]
binb = binb[::-1]
ans = ""
print(bina,binb)
dd = 2
for i in range(max(len(bina),len(binb))):
    print(i)
    if len(bina) <= i :
        da = 0
    else:
        da = int(bina[i])
    if len(binb) <= i :
        db = 0
    else:
        db = int(binb[i])
    nume = (abs(a - b) + 1)
    if i == 0:
        if nume % 2 == 0:
            ans = str((nume // 2) % 2)
        else:
            ans = str(((nume // 2) + db) % 2)
    else:
        fla = a // dd * dd
        ceila = (a // dd + 1) * dd
        flb = b // dd * dd
        ceilb = (b // dd + 1) * dd
        print(fla, ceila, flb,ceilb)
    dd = dd * 2
print(ans)
