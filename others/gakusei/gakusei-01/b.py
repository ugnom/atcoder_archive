words = lambda t : list(map(t, input().split()))
n,k = words(int)
a = words(int)

accum = [0] * n
adding = [0] * n

for i in range(n-1):
    for j in range(i,n):
        if a[i] > a[j]:
            adding[i] += 1

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            accum[i] += 1

MOD = 10**9 + 7
sum_accum = sum(accum)
sum_adding = sum(adding)
ans = 0

ans = (((k-1) * k) // 2) * sum_accum + k * sum_adding
ans %= MOD
'''
for i in range(k):
    ans += sum_accum * i + sum_adding
    ans %= MOD
'''
print(ans)
