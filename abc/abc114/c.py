import sys
sys.setrecursionlimit(2000)

n = int(input())

def dfs(is3, is5, is7, s):
    if s != "" and int(s) > n:
        return 0
    else:
        ans = 0
        if is3 and is5 and is7:
            ans += 1
        ans += dfs(True, is5, is7, s + "3")
        ans += dfs(is3, True, is7, s + "5")
        ans += dfs(is3, is5, True, s + "7")
    return ans

print(dfs(False,False,False,""))
