arr= list(map(int, input().split()))
sum_val = 0
cnt = 0

for i in range(len(arr)) :
    if arr[i] == 0 :
        break

    if arr[i] % 2 == 0 :
        cnt += 1
        sum_val += arr[i]

print(cnt, sum_val)