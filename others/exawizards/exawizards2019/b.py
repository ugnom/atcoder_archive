i = input()
s = input()

r = 0
b = 0
for c in s:
    if c == 'R':
        r += 1
    else:
        b += 1

if r > b:
    print("Yes")
else:
    print("No")
