A = input()


def modify(string) :
    arr = []
    arr_2 = []
    for i in string :
        arr.append(i)

    for j in range(len(arr)) :
        arr_2.append(arr[-1-1*j])

    if arr == arr_2 :
        return True

    else :
        return False

if modify(A) :
    print("Yes")

else :
    print("No")
    