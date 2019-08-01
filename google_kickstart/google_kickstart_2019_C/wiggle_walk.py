t = int(input())
for _ in range(t):
    case()

def case():
    n,r,c,sr,sc = list(map(int, input()))
    s = input()
    cur_r = sr
    cur_c = sc
    rs = [set() for _ in range(r)]
    re = [set() for _ in range(r)]
    cs = [set() for _ in range(c)]
    ce = [set() for _ in range(c)]
    rs[sr] = sc
    re[sr] = sc
    ss[sc] = sr
    se[sc] = sr
    for c in s:
        if c == "N":
            se[cur_c]
