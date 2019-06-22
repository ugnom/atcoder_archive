words = lambda t : list(map(t, input().split()))

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    return (x * y) // gcd(x,y)

def num_div(k,s):
    return s // k

a,b,c,d = words(int)

cd_lcm = lcm(c,d)

n_div_till_b = num_div(c,b) + num_div(d,b) - num_div(cd_lcm, b)
n_div_till_am1 = num_div(c,a-1) + num_div(d,a-1) - num_div(cd_lcm,a-1)

ans = (b-a+1) - n_div_till_b + n_div_till_am1

print(ans)
