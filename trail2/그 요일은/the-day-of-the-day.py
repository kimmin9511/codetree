m1, d1, m2, d2 = map(int, input().split())
A = input()

day_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
word = ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun']

month , day = m1, d1
_list = [0] * 7
count_day = 0

while True :
    # if (m1 == m2 and d1 == d2) or (month == m2 and day == d2) : month, day가 이미 m1, d1 값으로 지정되었으므로 필요없는 코드
    if (month == m2 and day == d2) :
        count_day += 1
        day += 1
    
# 위 코드에서 count_day > 7일 때, count_day가 7의 배수라면 _list[-1] += 1이 되는데, 의도한 것이 아니므로 코드 수정 후 통합.
        # if count_day <= 7 :
        #     _list[count_day-1] += 1
        #     break

        # elif count_day > 7 :
        #     _list[count_day % 7 -1] += 1
        #     break

        _list[(count_day - 1) % 7] += 1
        break


    count_day += 1
    day += 1
    
    # if count_day <= 7 :
    #     _list[count_day-1] += 1

    # elif count_day > 7 :
    #     _list[count_day % 7 -1] += 1

    _list[(count_day - 1) % 7] += 1

    if day > day_list[month] :
        month += 1
        day = 1

for i in word :
    if i == A :
        print(_list[word.index(i)])