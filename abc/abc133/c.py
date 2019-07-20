words = lambda t : list(map(t, input().split()))
l,r = words(int)

ml = l % 2019
mr = r % 2019

if ml >= mr or r - l >= 2019:
    print(0)
else:
    mi = (ml * (ml+1)) % 2019
    for i in range(ml,mr):
        for j in range(i+1, mr+1):
            #print(i,j,i*j,(i*j)%2019)
            mi = min(mi, (i*j) % 2019)
    print(mi)
