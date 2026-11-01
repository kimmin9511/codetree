n = input()
arr = []

for i in range(len(n)) :
    if i % 2 == 1 :
        arr.append(n[i])

for j in range(-1, -1*len(arr)-1, -1) :
    print(arr[j], end="")
        