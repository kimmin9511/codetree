n = input()

arr = list(n) 
arr_2 = []

a, b = arr[0], arr[1]

for i in arr :
    if i == a :
        i = b

    elif i == b :
        i = a

    arr_2.append(i)

str = ''.join(arr_2)

print(str)