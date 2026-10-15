x = list(map(int, input().split()))
x[0], x[1] = x[1], x[0]
print(x[0], x[1])