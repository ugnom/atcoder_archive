import numpy as np
from itertools import chain,combinations

words = lambda t : list(map(t, input().split()))

n,m = words(int)
ks = []
for i in range(m):
  ks.append(words(int))
  ks[i].pop(0)

ms = words(int)

#print(ks,ms)

def powerset(it):
  s = list(it)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

ans = 0
for s in powerset([i+1 for i in range(n)]):
  n_on = 0
  for k,mods in zip(ks,ms):
    n_inc = 0
    for ink in k:
      if ink in s:
        n_inc += 1
    if n_inc % 2 == mods:
      n_on += 1
  if n_on == m:
    ans += 1

print(ans)
