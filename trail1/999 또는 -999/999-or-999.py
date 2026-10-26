n = list(map(int, input().split()))
max_val = n[0]
min_val = n[0]

for i in n[1:] :
    if i == 999 or i == -999 :
        break

    if min_val > i :
        min_val = i

    if max_val < i :
        max_val = i

print(max_val, min_val)

    

