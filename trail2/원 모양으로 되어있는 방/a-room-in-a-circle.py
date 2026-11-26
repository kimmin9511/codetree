import sys
n = int(input())
a = [int(input()) for _ in range(n)]

INT_MAX = sys.maxsize
max_val = INT_MAX

for i in range(n) :
    result = 0

    if i == 0 :
        for j in range(n) :
            result += a[j] * j
        
    elif i == n-1 :
        for j in range(n-1) :
            result += a[j] * (j+1)

    else :
        for k in range(i) :
            result += a[k]*(n+k-i)

        for k in range(i+1, n) :
            result += a[k]*(k-i)


    if result <= max_val :
        max_val = result

print(max_val)