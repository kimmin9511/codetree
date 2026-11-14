m1, d1, m2, d2 = map(int, input().split())

month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count_day = 0

left_list = ['Sun', 'Sat', 'Fri', 'Thu','Wed', 'Tue', 'Mon']
right_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


if m1 > m2 :
    month, day = m2, d2
    
    while True :

        if month == m1 and day == d1 :
            num = count_day % 7
            print(left_list[num-1])
            break

        count_day += 1
        day += 1

        if day > month_list[month] :
            month += 1
            day = 1


elif m1 < m2 :
    month, day = m1, d1

    while True :

        if month == m2 and day == d2 :
            num = count_day % 7
            print(right_list[num])
            break

        count_day += 1
        day += 1

        if day > month_list[month] :
            month += 1
            day = 1

else :

    if d1 > d2 :
        count_day = d1 - d2
        num = count_day % 7
        print(left_list[num-1])
        
    elif d1 < d2 :
        count_day = d2 - d1
        num = count_day % 7
        print(right_list[num])
        
    else :
        print("Mon")
        


