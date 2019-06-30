words = lambda t : list(map(t, input().split()))
s = input()

if (s[0] == s[1] and s[2] == s[3] and not(s[0] == s[2])) or (s[0] == s[2] and s[1] == s[3] and not (s[0] == s[1])) or (s[0] == s[3] and s[1] == s[2] and not (s[0] == s[1])):
   print("Yes")
else:
    print("No")
