n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)


class info :
    def __init__(self, a, b, c) :
        self.day = a
        self.day_of_week = b
        self.weather = c


num_info = []

rain_idx = [i for i, w in enumerate(weather) if w == "Rain"]

for i in rain_idx :
    num_info.append(date[i])
    

num_info.sort()
find_num = num_info[0]

for i, j in enumerate(date) :
    if j == find_num and weather[i] == "Rain" :
        num = i
        break


rainy_day = info(date[num], day[num], weather[num])

print(f"{rainy_day.day} {rainy_day.day_of_week} {rainy_day.weather}")
    