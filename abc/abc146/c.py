words = lambda t : list(map(t, input().split()))
a,b,x = words(int)

import math
if a + b > x:
    print(0)
else:
    ans = 0
    for i in range(1,20):
        t_ans = (x - b*i) // a
        if t_ans <= 0:
            continue
        #print(t_ans)
        #print(i, math.floor(math.log(t_ans,10)) + 1)
        if i == math.floor(math.log(t_ans,10)) + 1:
            ans = max(ans,t_ans)
        elif i < math.floor(math.log(t_ans,10)) + 1:
            tt_ans = 0
            for j in range(i):
                tt_ans += 9*(10**j)
            ans = max(ans,tt_ans)
    print(min(ans, 1000000000))
