import math

words = lambda t : list(map(t, input().split()))
n = int(input())

x = n / 1.08
#print(x)
if math.floor(math.floor(x) * 1.08) == n:
    #print(1)
    print(math.floor(x))
elif math.floor(math.ceil(x) * 1.08) == n:
    #print(2)
    print(math.ceil(x))
else:
    print(":(")
