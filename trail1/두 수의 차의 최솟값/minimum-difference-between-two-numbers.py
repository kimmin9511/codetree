n = int(input())

arr = list(map(int, input().split()))

min = arr[n-1]

for i in range(n) :
    for j in range(n) :
        if i< j :
            if arr[j] - arr[i] < min :
                min = arr[j] - arr[i]

print(min)