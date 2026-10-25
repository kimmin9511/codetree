arr = list(map(int, input().split()))
sum_val = 0
cnt  = 0

for i in range(len(arr)) :
    if arr[i] == 0 :
        break

    sum_val +=arr[i]
    cnt += 1

print(sum_val, end=" ")

print(f"{(sum_val/cnt):.1f}")

    