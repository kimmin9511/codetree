arr = list(map(int, input().split()))
arr2 = list()

n = len(arr)


for i in range(n) :
    if arr[i] == 0 :
        break

    arr2.append(arr[i])

for j in arr2[::-1] :
    print(j, end=" ")



    





    