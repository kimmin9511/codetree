arr = [0 for _ in range(4)]

for i in range(3) :
    a, b = map(str, input().split())
    b = int(b)
    if a == 'Y' :
        if b >= 37 :
            arr[0] += 1

        else :
            arr[2] += 1

    elif a == 'N' :
        if b >= 37 :
            arr[1] += 1

        else :
            arr[3] += 1

for i in range(0, 4) :
    print(f"{arr[i]}", end=" ")

if arr[0] >= 2 :
    print("E")