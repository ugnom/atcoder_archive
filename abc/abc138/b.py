words = lambda t : list(map(t, input().split()))
n = int(input())
a = words(int)

print(1 / sum(map(lambda x: 1/x, a)))
