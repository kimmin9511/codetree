n = int(input())
a = list(map(int, input().split()))

print(max(a), end=" ")

idx = a.index(max(a))

a.pop(idx)

print(max(a))

