import sys

n = int(input())
numbers = list(map(int, input().split()))

INT_MIN = -sys.maxsize

max_val = INT_MIN

for i in range(n-2) :
    for j in range(i+2, n) :
        if numbers[i] + numbers[j] >= max_val :
            max_val = numbers[i] + numbers[j]

print(max_val)
