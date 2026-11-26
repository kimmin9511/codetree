import sys
a = input()

arr = []

for num in a :
    arr.append(num)

INT_MAX = -sys.maxsize
max_val = INT_MAX

if len(a) == 1 :
    max_val = 0

else :
    for i in range(1, len(arr)) :
        result = 0
        if arr[i] == '1' :
            arr[i] = '0'

        else :
            arr[i] = '1'

        for j in arr :
            result = result * 2 + int(j)

        if result >= max_val :
            max_val = result

        if arr[i] == '1' :
            arr[i] = '0'

        else :
            arr[i] = '1'

print(max_val)

