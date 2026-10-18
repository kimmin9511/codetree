cnt = 0

cnt2 = 0

for i in range(10) :
    n = int(input())

    if n % 3 == 0 and n % 5 != 0 :
        cnt += 1

    elif n % 3 != 0 and n % 5 == 0 :
        cnt2 += 1

    elif n % 3 == 0 and n % 5 == 0 :
        cnt += 1
        cnt2 += 1

print(cnt, end=" ")

print(cnt2)
    