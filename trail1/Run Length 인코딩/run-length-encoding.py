A = input()

cnt = 1

arr = [A[0]]

for i in range(1, len(A)) :

    if A[i-1] == A[i] :
        cnt+=1

    else :
        word = A[i]
        arr.append(cnt)
        arr.append(word)
        cnt = 1

arr.append(cnt)

sum = 0
for elem in arr :
    sum += len(str(elem))

print(sum)

for elem in arr :
    print(elem, end="")




