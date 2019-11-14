s = input()
a = list(map(lambda s: s.split("*"), s.split("+")))
#print(a)

ans = 0
for c in a:
    need0 = True
    for e in c:
        #print(c,e)
        if e == "0":
            #print(c,e)
            need0 = False
            break
    if need0:
        ans += 1
print(ans)
