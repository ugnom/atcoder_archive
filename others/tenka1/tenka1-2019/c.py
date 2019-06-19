words = lambda t : list(map(t, input().split()))
n = int(input())
s = input()

zo = []
zcnt = 0
ocnt = 0
for c in s:
    if c == "#":
        zo.append(1) #black
        ocnt += 1
    else:
        zo.append(0) #white
        zcnt += 1

#print(zcnt,ocnt)
minans = min(ocnt,zcnt)
zcnttill = 0
ocnttill = 0
for i in range(0,n):
    if zo[i] == 0:
        zcnttill += 1
    else:
        ocnttill += 1
    minans = min(minans, ocnttill + (zcnt - zcnttill))

print(minans)
