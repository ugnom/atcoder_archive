words = lambda t : list(map(t, input().split()))
n = int(input())
s = input()

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def conv(c,n):
    co = ord(c)
    co += n
    if co > 90:
        co -= 26
    #print(co)
    return chr(co)

ans = ""
for c in s:
    ans += conv(c,n)
print(ans)
