n = int(input())
a = list(map(int, input().split()))

max_val = a[0]

for i in a :
    if max_val < i :
        max_val = i

print(max_val, end=" ")

max_idx = a.index(max_val)
a.pop(max_idx)

max_val2 = a[0]

for i in a :
    if max_val2 < i :
        max_val2 = i

print(max_val2)
