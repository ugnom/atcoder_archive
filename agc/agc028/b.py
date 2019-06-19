

def factorial(n):
    ret = 1
    for i in range(n):
        ret = ret * (i+1)
    return ret

def main():
    n = int(input())
    a = list(map(int, input().split()))
    fac = factorial(n)
    #print("fac", fac)
    sum = 0
    base = 0
    for i in range(2,n+2):
        base = base + i
    print(base)
    for i in range(n):
        #print((abs(j-i)+1), )
        base = base + (i+1) - (n)
        #sum = sum + (a[i] * fac) // (abs(j - i) + 1
        print(base)
        sum = sum + (a[i] * fac) // base
        sum = sum % (10**9 + 7)
    print(sum)


if __name__ == "__main__":
    main()
