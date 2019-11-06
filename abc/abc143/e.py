words = lambda t : list(map(t, input().split()))
n,m = words(int)

dp = [-1] * (2**n)
dp[0] = 0

def to_bits(xs):
    bits = 0
    for x in xs:
        bits += 2**(x-1)
    return bits

costs = []
bits = []
for i in range(m):
    c,k = words(int)
    costs.append(c)
    ys = words(int)
    bits.append(to_bits(ys))

#print(costs)
#print(bits)

for cur in range(2**n):
    if dp[cur] == -1:
        continue
    #print(dp)
    for c,b in zip(costs, bits):
        next = cur | b
        if dp[next] == -1 or dp[next] > dp[cur] + c:
            dp[next] = dp[cur] + c

print(dp[2**n-1])
