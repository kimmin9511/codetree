arr = [
    input() for i in range(11)
]

word = arr[10]
cnt = 0

for i in range(10) :
    if arr[i][-1] == word :
        print(arr[i])
        cnt += 1

if cnt == 0 :
    print("None")

    