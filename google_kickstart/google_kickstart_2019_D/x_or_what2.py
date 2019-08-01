from functools import reduce

def main():
    t = int(input())
    for i in range(t):
        case(i)

def xor_cnt(x):
    cnt = 0
    digit = 1024
    while x != 0:
        if x >= digit:
            cnt += 1
            x -= digit
        digit = digit // 2
    return cnt % 2

def find_first_bit(b):
    left = 0
    for i in range(len(b)):
        if b[i] == 1:
            break
        left+=1
    right = len(b) - 1
    for i in range(len(b)-1,-1,-1):
        if b[i] == 1:
             break
        right-= 1
    return left,right


words = lambda tp: list(map(tp,input().split()))

def decide_ans(length, cnt, left, right):
    if cnt == 0:
        return length
    else:
        return length - (min(left,length-right-1)+1)

def case(k):
    ans = []
    n,q = words(int)
    a = words(int)
    a = list(map(xor_cnt, a))
    cnt = a.count(1) % 2
    left, right = find_first_bit(a)
    #print(k, " log1: ", cnt,left,right)
    for _ in range(q):
        p,v = words(int)
        v = xor_cnt(v)
        #print(k, "log ", p, v, left, right, cnt)
        if a[p] == v:
            ans.append(decide_ans(len(a), cnt, left, right))
        else:
            if 0 <= p < left:
                # always v == 1:
                left = p
            elif p == left:
                # always v == 0:
                cand = left+1
                while cand < len(a) and a[cand] == 0:
                    cand += 1
                left = cand
            elif p == right:
                cand = right-1
                while cand >= 0 and a[cand] == 0:
                    cand -= 1
                right = cand
            elif right < p < len(a):
                right = p
            cnt = (cnt + 1) % 2
            ans.append(decide_ans(len(a),cnt,left,right))

        a[p] = v

    print("Case #" + str(k+1) + ": " + " ".join(list(map(str,ans))))


if __name__ == '__main__':
    main()
