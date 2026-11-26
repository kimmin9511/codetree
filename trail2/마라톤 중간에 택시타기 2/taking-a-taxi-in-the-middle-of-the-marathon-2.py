import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

INT_MAX = sys.maxsize
min_val = INT_MAX

for i in range(1, n-1) :
    result = 0
    a = x.pop(i)
    b = y.pop(i)
    
    for j in range(1, n-1) :
        result += abs(x[j] - x[j-1]) + abs(y[j]-y[j-1])

    if result <= min_val :
        min_val = result

    x.insert(i, a)
    y.insert(i, b)
    
print(min_val)