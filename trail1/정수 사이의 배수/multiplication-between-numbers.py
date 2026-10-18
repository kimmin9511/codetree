a, b = map(int, input().split())
sum_val = 0
sum_cnt = 0

for i in range(a, b+1) :
    if i % 5 == 0 or i % 7 == 0 :
        sum_val += i
        sum_cnt += 1

print(sum_val, end=" ")
print(f"{(sum_val / sum_cnt):.1f}")