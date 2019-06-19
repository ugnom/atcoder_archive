import numpy as np
words = lambda t : list(map(t, input().split()))
n = int(input())
ws = words(int)

less = 0
more = sum(ws)

ans = abs(more-less)
for i in range(n):
    less += ws[i]
    more -= ws[i]
    ans = min(ans, abs(more-less))

print(ans)
