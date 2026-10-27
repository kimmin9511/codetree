n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

b = [
    list(map(int, input().split()))
    for _ in range(n)
]

c = [
    [0 for _ in range(m)] for _ in range(n) 
]

for i in range(n) :
    for j in range(m) :
        result = 1
        if a[i][j] == b[i][j] :
            result = 0
        
        c[i][j] = result

        print(c[i][j], end=" ")

    print()

