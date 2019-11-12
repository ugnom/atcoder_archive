n,m = list(map(int, input().split()))

def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    divs.sort()
    return divs

divs = divisors(m)
ans = 1
for d in divs:
    if m // d >= n:
        ans = d
print(ans)
