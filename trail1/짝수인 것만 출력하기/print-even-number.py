n = int(input())

arr = list(map(int, input().split()))

a = []

for i in range(n) :
    if arr[i] % 2 == 0 :
        a.append(arr[i])

for i in a :
    print(i, end=" ")
