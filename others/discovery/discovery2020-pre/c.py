words = lambda t : list(map(t, input().split()))
h,w,k = words(int)
mat = []
w_empty = []
for i in range(h):
    wi = input()
    mat.append(wi)
    emp = True
    for ww in wi:
        if ww == "#":
            emp = False
            break
    w_empty.append(emp)

ans = [[0] * w for i in range(h)]
ki = 1
i = 0
stt = 0
lastMark = 0
while i < h:
    while i < h and w_empty[i]:
        i+=1
    if i >= h:
        break
    lastSharp = 0
    for j in range(w):
        for k in range(stt,i+1):
            ans[k][j] = ki
            if mat[k][j] == "#":
                ki += 1
                lastSharp = j
    for j in range(lastSharp,w):
        for k in range(stt,i+1):
            ans[k][j] = ki-1
    #print(i, "----------------------")
    #for wi in ans:
    #    print(" ".join((list(map(str,wi)))))
    lastMark = i
    i+=1
    stt = i

for j in range(lastMark+1,h):
    for k in range(w):
        ans[j][k] = ans[lastMark][k]

for wi in ans:
    print(" ".join((list(map(str,wi)))))
