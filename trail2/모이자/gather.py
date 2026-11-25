import sys

n = int(input())
A = list(map(int, input().split()))

arr = []

for k in range(n) :
    arr.append(k)

INT_MAX = sys.maxsize
min_val = INT_MAX

for i in range(n) :
    sum = 0

    for j in range(n) :
        sum += A[j] * abs(arr[j]-arr[i])

    if sum < min_val :
        min_val = sum

print(min_val)

