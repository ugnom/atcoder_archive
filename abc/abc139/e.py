import heapq

words = lambda t : list(map(lambda x : t(x)-1, input().split()))
n = int(input())

a = []
for i in range(n):
    a.append(words(int))

heap = []
for i in range(n):
    heapq.heappush(heap, (1,i))
cur_day = [1] * n
cur_ind = [0] * n

looping = False
looping_det = (0,0)
suc = True
while len(heap) > 0:
    (d, p) = heapq.heappop(heap)
    if d < cur_day[p]:
        continue
    ind = cur_ind[p]
    oth = a[p][ind]
    if a[oth][cur_ind[oth]] == p:
        looping = False
        play_day = max(cur_day[oth], d)
        cur_day[oth] = play_day+1
        cur_day[p] = play_day+1
        cur_ind[p] += 1
        cur_ind[oth] += 1
        if cur_ind[p] < n-1:
            heapq.heappush(heap, (play_day+1, p))
        if cur_ind[oth] < n-1:
            heapq.heappush(heap, (play_day+1, oth))
    else:
        if looping == True and (d,p) == looping_det:
            suc = False
            break
        if looping != True:
            looping = True
            looping_det = (d+1, p)
        heapq.heappush(heap, (d+1, p))
ans = 0
if suc:
    for i in range(n):
        ans = max(ans, cur_day[i])
    print(ans-1)
else:
    print(-1)
