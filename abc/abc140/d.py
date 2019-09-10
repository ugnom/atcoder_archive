import copy

words = lambda t : list(map(t, input().split()))
n,k = words(int)
s = input()

if n == 1:
    print(0)
    exit()

t = list(copy.copy(s))
x = k
i = 0
while i < len(t) and t[i] == "L":
    i += 1
while x > 0 and i < len(t):
    if t[i] == "L":
        x -= 1
        while i < len(t) and t[i] == "L":
            t[i] = "R"
            i+=1
    else:
        i+= 1

if x > 0 and t[0] == "L":
    i = 0
    while i < len(t) and t[i] == "L":
        t[i] = "R"
        i += 1

#print(t)
def calcAns(t):
    ans = 0
    for i in range(1,len(t)-1):
        #print(t[i])
        if t[i] == "L":
            if t[i-1] == "L":
                ans += 1
        elif t[i] == "R":
            if t[i+1] == "R":
                ans += 1
    if t[0] == "R" and t[1] == "R":
        ans += 1
    if t[-1] == "L" and t[-2] == "L":
        ans += 1
    return ans

ansR = calcAns(t)
#print(ansR)

t = list(copy.copy(s))
x = k
i = 0
while i < len(t) and t[-(i+1)] == "R":
    i += 1

while x > 0 and i < len(t):
    if t[-(i+1)] == "R":
        x -= 1
        while i < len(t) and t[-(i+1)] == "R":
            t[-(i+1)] = "L"
            i+=1
    else:
        i+= 1

if x > 0 and t[-1] == "R":
    i = 0
    while i < len(t) and t[-(i+1)] == "R":
        t[-(i+1)] = "L"
        i += 1

#print(t)
ansL = calcAns(t)
#print(ansL)

print(max(ansL,ansR))
