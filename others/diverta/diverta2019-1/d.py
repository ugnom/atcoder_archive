words = lambda t : list(map(t, input().split()))
n = int(input())

total = 0
for i in range(1,n):
    #print("check", (n-i)//i, i)
    if (n-i) // i <= i:
        #print("end", n//i, i)
        break
    if (n-i) % i == 0:
        #print(n-i,i)
        total += (n-i) // i

print(total)
