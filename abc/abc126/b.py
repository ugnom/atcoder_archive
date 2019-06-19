import numpy as np
words = lambda t : list(map(t, input().split()))

str = input()

first = int(str[:2])
second = int(str[2:])

firstY = True
firstM = 1 <= first and first <= 12
secondY = True
secondM = 1 <= second and second <= 12

if firstM and secondM:
    print("AMBIGUOUS")
elif firstM:
    print("MMYY")
elif secondM:
    print("YYMM")
else:
    print("NA")
