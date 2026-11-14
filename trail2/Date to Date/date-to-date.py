m1, d1, m2, d2 = map(int, input().split())

month, day = m1, d1
count_day = 1
day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True :
    if month == m2 and day == d2 :
        break

    count_day += 1
    day += 1

    if day > day_list[month] :
        month += 1
        day = 1


print(count_day)


