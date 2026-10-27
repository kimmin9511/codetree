arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2) :
    val_1 = 0
    for j in range(4) :
        val_1 += arr[i][j]

    print(f"{(val_1/4):.1f}", end=" ")

print()

for i in range(4) :
    val_2 = 0
    for j in range(2) :
        val_2 += arr[j][i]

    print(f"{(val_2/2):.1f}", end=" ")

print()

val_3 = sum(sum(i) for i in arr)

print(f"{(val_3/8):.1f}")

    

    
        