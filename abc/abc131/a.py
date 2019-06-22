words = lambda t : list(map(t, input().split()))
s = input()
bad = False
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        bad = True
        break

if bad:
    print("Bad")
else:
    print("Good")
