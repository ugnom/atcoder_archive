words = lambda t : list(map(t, input().split()))
k = int(input())
x,y = words(int)

ans = []
cur = (x,y)
cnt = 0
done = True
while True:
    if cur[0] == x and cur[1] == y:
        break
    cnt += 1
    if cur[0] != x:
