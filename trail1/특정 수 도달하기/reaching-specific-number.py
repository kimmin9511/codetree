n = list(map(int, input().split()))

sum_val = 0
cnt  = 0

for i in range(len(n)) :
    if n[i] >= 250 :
        break
    
    sum_val += n[i]
    cnt += 1

print(sum_val, end=" ")
print(f"{(sum_val / cnt):.1f}")