import fractions as math

def lcm(x,y):
    return (x * y) // math.gcd(x,y)

def main():
    (n,m) = map(int, input().split())
    s = input()
    t = input()

    nmlcm = lcm(n,m)
    nn = nmlcm // n
    mm = nmlcm // m
    nnmmlcm = lcm(nn,mm)

    for i in range(nmlcm // nnmmlcm):
        #print(nnmmlcm*i)
        if s[nnmmlcm*i//nn] != t[nnmmlcm*i//mm]:
            print(-1)
            return
    print(nmlcm)

if __name__ == "__main__":
    main()
