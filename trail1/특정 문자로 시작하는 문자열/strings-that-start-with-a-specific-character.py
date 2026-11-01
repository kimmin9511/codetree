n = int(input())

arr = [
    input() for _ in range(n)
]

word = input()

sum = 0
cnt = 0

for i in range(n) :
    if arr[i][0] == word :
        sum += len(arr[i]) 
        cnt += 1

print(f"{cnt} {(sum/cnt):.2f}")
