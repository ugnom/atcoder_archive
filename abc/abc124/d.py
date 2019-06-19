import numpy as np
words = lambda t : list(map(t, input().split()))

n,k =  words(int)
s = input()

stt = s[0]

cnts = []
cur = stt
lcnt = 0
for c in s:
    if c == cur:
        lcnt += 1
    else:
        cnts.append(lcnt)
        lcnt = 1
        if cur == '0':
            cur = '1'
        else:
            cur = '0'
cnts.append(lcnt)
zsum = 0
if stt == '0':
    sumstt = 1
    for i in range(min(k*2,len(cnts))):
        zsum += cnts[i]
else:
    sumstt = 0

#print(cnts)
sum = 0
#print("ss",sumstt, len(cnts),sumstt+(k*2+1))
for i in range(sumstt, min(len(cnts),sumstt+(k*2+1))):
    sum += cnts[i]

#print(zsum, sum)
maxsum = max(zsum,sum)

l = sumstt + 2
r = sumstt + k*2+1 + 2
#print("first lr",l,r)
while r <= len(cnts):
    sum = sum - cnts[l-2] - cnts[l-1] + cnts[r-2] + cnts[r-1]
    #print(l,r, sum)
    maxsum = max(maxsum, sum)
    l += 2
    r += 2

#print(l,r)
if s[-1] == '0' and r-2 < len(cnts):
    sum = sum - cnts[l-2] - cnts[l-1] + cnts[r-2]
    #print("last 0", l, r,sum)
    maxsum = max(maxsum, sum)

print(maxsum)
