words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

i = 1
j = n-2
left = a[0]
right = a[-1]
while i <= j:
    if left >= right:
        right += a[j]
        j -= 1
    else:
        left += a[i]
        i += 1

print(abs(left-right))
