arr = list(map(int, input().split()))
new = []

for i in arr :
    if i == 0 :
        break

    elif i % 2 == 1 :
        i += 3

    else :
        i = i//2

    new.append(i)

for i in new :
    print(i, end=" ")
    

    