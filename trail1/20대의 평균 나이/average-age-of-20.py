sum_val = 0
sum_cnt = 0

while True :
    n = int(input())

    if n >= 20 and n < 30 :
        sum_val += n
        sum_cnt += 1

    else :
        break

print(f"{(sum_val/sum_cnt):.2f}")

