import sys
words = lambda t : list(map(t, input().split()))
n = int(input())
INF = sys.maxsize
MINF = -sys.maxsize-1

max_x_l = MINF
min_x_l = INF
max_x_r = MINF
min_x_r = INF
max_x_s = MINF
min_x_s = INF
max_y_u = MINF
min_y_u = INF
max_y_d = MINF
min_y_d = INF
max_y_s = MINF
min_y_s = INF

for i in range(n):
    cx,cy,d = input().split()
    x = int(cx)
    y = int(cy)
    if d == 'U':
        max_y_u = max(max_y_u, y)
        min_y_u = min(min_y_u, y)
        max_x_s = max(max_x_s, x)
        min_x_s = min(min_x_s, x)
    elif d == 'D':
        max_y_d = max(max_y_d, y)
        min_y_d = min(min_y_d, y)
        max_x_s = max(max_x_s, x)
        min_x_s = min(min_x_s, x)
    elif d == 'L':
        max_y_s = max(max_y_s, y)
        min_y_s = min(min_y_s, y)
        max_x_l = max(max_x_l, x)
        min_x_l = min(min_x_l, x)
    elif d == 'R':
        max_y_s = max(max_y_s, y)
        min_y_s = min(min_y_s, y)
        max_x_r = max(max_x_r, x)
        min_x_r = min(min_x_r, x)
