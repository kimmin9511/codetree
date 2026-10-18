n = int(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0

for i in range(1, n+1) :
    if i % 2 == 0 and i % 3 != 0 and i % 12 != 0 :
        cnt_1 += 1

    elif i % 2 == 0 and i % 3 == 0 and i % 12 != 0 : 
        cnt_2 += 1

    elif i % 2 != 0 and i % 3 == 0 and i % 12 != 0 : 
        cnt_2 += 1

    elif i % 2 == 0 and i % 3 == 0 and i % 12 == 0 :
        cnt_3 += 1

print("{} {} {}".format(cnt_1, cnt_2, cnt_3))
