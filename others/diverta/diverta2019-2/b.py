words = lambda t : list(map(t, input().split()))
n = int(input())
xys = []
for i in range(n):
    (x,y) = words(int)
    xys.append((x,y))

min_score = -1
for i in range(n):
    xy1 = xys[i]
    for j in range(i,n):
        a = set(xys)
        xy2 = xys[j]
        p = xy1[0] - xy2[0]
        q = xy1[1] - xy2[1]
        score = 0
        while len(a) > 0:
            score += 1
            (x,y) = a.pop()
            xup = x + p
            yup = y + q
            while (xup,yup) in a:
                a.remove((xup,yup))
                xup += p
                yup += q
            xdn = x - p
            ydn = y - q
            while (xdn,ydn) in a:
                a.remove((xdn,ydn))
                xdn -= p
                ydn -= q
        if min_score == -1:
            min_score = score
        else:
            min_score = min(min_score,score)
print(min_score)
