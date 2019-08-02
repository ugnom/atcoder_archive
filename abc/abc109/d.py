words = lambda t : list(map(t, input().split()))
h,w = words(int)
mat = []
for _ in range(h):
    mat.append(words(int))
ans = []

for i in range(h-1):
    for j in range(w):
        if mat[i][j] % 2 != 0:
            mat[i][j] -= 1
            mat[i+1][j] += 1
            ans.append([i+1,j+1,i+2,j+1])
for i in range(w-1):
    if mat[-1][i] % 2 != 0:
        mat[-1][i] -= 1
        mat[-1][i+1] += 1
        ans.append([h,i+1,h,i+2])

print(len(ans))
for a in ans:
    print(" ".join(map(str,a)))
