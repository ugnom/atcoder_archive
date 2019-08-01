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
        left+=1
        if b[i] == 1:
            break
    right = 0
    for i in range(len(b)-1,-1,-1):
        right+=1
        if b[i] == 1:
             break
    return left,right

def find_max_subint(b):
    if b.count(1) % 2 == 0:
        return (0, 0)
    else:
        left = 0
        for i in range(len(b)):
            left+=1
            if b[i] == 1:
                break

        right = 0
        for i in range(len(b)-1,-1,-1):
            right+=1
            if b[i] == 1:
                break
        if left > right:
            return (right, 1)
        elif left < right:
            return (left, -1)
        else:
            return (left, 0)

words = lambda tp: list(map(tp,input().split()))
def case(k):
    ans = []
    n,q = words(int)
    a = words(int)
    a = list(map(xor_cnt, a))
    max_intvl, direction = find_max_subint(a)
    for _ in range(q):
        p,v = words(int)
        v = xor_cnt(v)
        if a[p] == v:
            ans.append(len(a) - max_intvl)
        else:
            if max_intvl != 0:
                ans.append(len(a))
                max_intvl = 0
                direction = 0
            else:
                a[p] = v
                max_intvl, direction = find_max_subint(a)
                ans.append(len(a)-max_intvl)
        a[p] = v
    print("Case #" + str(k+1) + ": " + " ".join(list(map(str,ans))))

def decide_ans(length, cnt, left, right):
    if cnt == 0:
        return length
    else:
        return length - min(left,right)

def case2(k):
    ans = []
    n,q = words(int)
    a = words(int)
    a = list(map(xor_cnt, a))
    cnt = b.count(1) % 2
    left, right = find_first_bit(a)
    for _ in range(q):
        p,v = words(int)
        v = xor_cnt(v)
        if a[p] == v:
            ans.append(ans[-1])
        else:
            if 0 <= p < left:
                # always v == 1:
                left = p
                ans.append()
            elif p == left:
                # always v == 0:
                cand = left+1
                while a[cand] == 0:
                    cand += 1
                left = cand
            elif p == right:
                cand = right-1
                while a[cand] == 0:
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
