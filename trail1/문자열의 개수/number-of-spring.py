cnt = 0
arr = []

while True :
    x = input()

    if x == '0' :
        break

    else :
        cnt += 1
        if cnt % 2 == 1 :
            arr.append(x)

print(cnt)
for i in arr :
    print(i, end="\n")
