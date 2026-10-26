arr = list(map(int, input().split()))

val_1 = min(arr)
val_2 = max(arr)

for i in arr :
    if i < 500 and val_1 < i :
        val_1 = i

    if i > 500 and val_2 > i :
        val_2 = i

print(val_1, val_2)
