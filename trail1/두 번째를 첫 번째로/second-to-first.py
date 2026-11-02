n = input()

arr = list(n) 
k = arr[1]

for i in range(1, len(arr)) :
    if arr[i] == k :
        arr[i] = arr[0]

str = ''.join(arr)

print(str)