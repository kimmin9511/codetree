n, q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(q) :
    quest = list(map(int, input().split()))

    if quest[0] == 1 :
        print(arr[quest[1]-1])

    elif quest[0] == 2 :
        for j in arr :
            if j == quest[1] :
                print(arr.index(j)+1)
                break

            if arr.count(quest[1]) == 0 :
                print(0)
                break


    elif quest[0] == 3 :
        for k in range(quest[1], quest[2]+1) :
            print(arr[k-1], end=" ")

        print()




