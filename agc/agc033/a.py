import functools as ft

h,w = map(int, input().split())
mat = [[True] * (w+2)]
for _ in range(h):
    mat.append([True] + [a == '#' for a in input()] + [True])
mat.append([True]*(w+2))

prev = []
for i in range(1,h+1):
    for j in range(1,w+1):
        if mat[i][j]:
            prev.append((i,j))



round = -1
while prev:
    round += 1
    #print(prev)
    #print(mat)
    def calc(next, tup):
        x = tup[0]
        y = tup[1]
        if not mat[x-1][y]:
            next.append((x-1,y))
            mat[x-1][y] = True
        if not mat[x][y-1]:
            next.append((x,y-1))
            mat[x][y-1] = True
        if not mat[x+1][y]:
            next.append((x+1,y))
            mat[x+1][y] = True
        if not mat[x][y+1]:
            next.append((x,y+1))
            mat[x][y+1] = True
        return next
    next = ft.reduce(calc, prev, [])

    prev = next

print(round)
