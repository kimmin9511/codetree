n = int(input())

arr = [1, n]

while True :
    arr.append(arr[-2]+arr[-1])

    if arr[-1] >= 100 :
        break

for i in arr :
    print(i, end=" ")