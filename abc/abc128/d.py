import numpy as np
words = lambda t : list(map(t, input().split()))

n,k = words(int)
vs = words(int)
#print(vs)
ans = 0
if True: # k < n:
    for i in range(k+1):
        #print("--------------")
        r = k-i
        #print(i,r)
        if i > n:
            continue
        for j in range(-1,i):
            temp = []
            for l in range(i):
                #print(j-l)
                temp.append(vs[j-l])
            temp.sort()
            #print(temp)
            for _ in range(r):
                if len(temp) == 0:
                    break
                if temp[0] < 0:
                    temp.pop(0)
                else:
                    break
            ss = sum(temp)
            ans = max(ans, ss)


print(ans)
