n = int(input())
sum_val = 0
sum_cnt = 0

for i in range(n) :
    x = int(input())
    sum_val += x
    sum_cnt += 1

print(sum_val, end=" ")
print(f"{(sum_val / sum_cnt):.1f}")