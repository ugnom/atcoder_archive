
import numpy as np
words = lambda t : np.array(list(map(t, input().split())))

words = lambda t : list(map(t, input().split()))

def solve(x) :
  return x

x = int(input())
print(solve(x))

x = int(input())
if solve(x) :
  print("YES")
else:
  print("NO")

t = int(input())
li = list(map(int,input().split()))
print(solve(li))
