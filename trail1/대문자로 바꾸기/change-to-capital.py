arr = [
    list(map(str, input().split()))
    for i in range(5)
]

result = [[i.upper() for i in j] for j in arr]

for i in result :
    for j in i :
        print(j, end=" ")

    print()


