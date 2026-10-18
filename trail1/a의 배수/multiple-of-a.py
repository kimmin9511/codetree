n, a = map(int, input().split())
count = 1

while count <= n :
    if count % a == 0:
        print(1)

    else :
        print(0)

    count+=1