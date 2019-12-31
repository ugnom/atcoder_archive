words = lambda t : list(map(t, input().split()))
n = int(input())
if n % 3 == 0:
    for i in range(n//3):
        s = ""
        for j in range(n//3):
            s += "aa."
        print(s)
        for k in range(2):
            s = ""
            for j in range(n//3):
                s += "..a"
            print(s)
elif n % 5 == 0:
    for i in range(n//5):
        s = ""
        for j in range(n//5):
            s += "aa.a."
        print(s)
        s = ""
        for j in range(n//5):
            s += "..ba."
        print(s)
        s = ""
        for j in range(n//5):
            s += "..b.c"
        print(s)
        s = ""
        for j in range(n//5):
            s += "aa..c"
        print(s)
        s = ""
        for j in range(n//5):
            s += "..bb."
        print(s)

else:
    print(-1)
