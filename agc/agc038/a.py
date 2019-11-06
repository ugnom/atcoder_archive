words = lambda t : list(map(t, input().split()))
h,w,a,b = words(int)

def composeM(h,w,a,b):
    ans = [[0]*w for i in range(h)]

    if a != 0 and b != 0:
        stt = 0
        for hi in range(h):
            for i in range(stt,stt+a):
                ans[hi][i%w] = 1
            stt += a
            stt %= w
    elif a == 0 and b != 0:
        for i in range(b):
            ans[i] = [1]*w
    elif a != 0 and b == 0:
        for i in range(a):
            for j in range(h):
                ans[j][i] = 1
    return ans
#print(ans)

ans = composeM(h,w,a,b)

k = []
for wi in range(w):
    cnt = 0
    for hi in range(h):
        if ans[hi][wi] == 1:
            cnt += 1
    if cnt != b and (h-cnt) != b:
        if k != empty:
            x = k[0]

cntw = [0]*w
def validate(ans,h,w,a,b):
    valid = True
    for wi in range(w):
        cnt = 0
        for hi in range(h):
            if ans[hi][wi] == 1:
                cntw[wi] += 1
            valid = False
    return valid

if validate(ans,h,w,a,b):
    for i in range(h):
        print("".join(map(str,ans[i])))
else:
        print("No")
