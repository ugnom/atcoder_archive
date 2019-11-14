sx,sy,tx,ty = list(map(int,input().split()))

ans = ""
for i in range(tx-sx):
    ans += "R"
for i in range(ty-sy):
    ans += "U"
for i in range(tx-sx):
    ans += "L"
for i in range(ty-sy):
    ans += "D"
ans += "D"
for i in range(tx-sx+1):
    ans += "R"
for i in range(ty-sy+1):
    ans += "U"
ans += "L"
ans += "U"
for i in range(tx-sx+1):
    ans += "L"
for i in range(ty-sy+1):
    ans += "D"
ans += "R"
print(ans)
