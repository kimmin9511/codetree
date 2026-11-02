cnt_1, cnt_2 = 0, 0

n = input()

for i in range(len(n)-1) :
    if n[i] == 'e' and n[i+1] == 'e' :
        cnt_1 += 1

    elif n[i] == 'e' and n[i+1] == 'b' :
        cnt_2 += 1

print(cnt_1, cnt_2)