sum_val = 0
sum_cnt = 0

for i in range(10) :
    n = int(input())

    if n >= 0 and n<=200 :
        sum_val += n
        sum_cnt += 1

print(sum_val, end=" ")

print(f"{(sum_val / sum_cnt):.1f}")