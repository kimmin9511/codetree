import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

INT_MAX = sys.maxsize
max_val = INT_MAX

for i in range(N) :
    for j in range(i+1, N) :
        sum = 0
        x = arr.pop(i)
        y = arr.pop(j-1)

        for k in range(len(arr)) :
            sum += arr[k]

        if abs(sum - S) <= max_val :
            max_val = abs(sum - S)

        arr.insert(i, x)
        arr.insert(j, y)

print(max_val)
