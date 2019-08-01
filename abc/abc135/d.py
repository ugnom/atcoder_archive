words = lambda t : list(map(t, input().split()))
s = input()
rs = reversed(s)

a = []
cur_mod_10_pow = 1
v = 0
for i,c in enumerate(rs):
    if c == "?":
        a.append(cur_mod_10_pow)
    else:
        v += (int(c) * cur_mod_10_pow) % 13
        v %= 13
    cur_mod_10_pow *= 10
    cur_mod_10_pow %= 13

#print(v, list(reversed(a)))
MOD = 1000000007
prev = [0] * 13
prev[0] = 1
#print(prev)
for aa in a:
    cur = [0 for _ in range(13)]
    for i,p in enumerate(prev):
        #print(i,p, cur)
        for j in range(10):
            #print(i,j,(i+aa*j) % 13)
            cur[(i+(aa*j)) % 13] += p
            cur[(i+aa*j) % 13] %= MOD
    #print(cur)
    prev = cur

print(prev[(5-v)%13])
