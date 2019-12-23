s = input()
d = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in range(len(d)):
    if s == d[i]:
        print(7-i)
        break
