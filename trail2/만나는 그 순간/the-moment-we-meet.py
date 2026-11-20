n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

a_list = []
b_list = []

start_a = 0
start_b = 0

for i in range(n) :
    if d[i] == 'R' :
        if i == 0 :
            for j in range(start_a, t[i] + 1) :
                a_list.append(j)

            start_a = t[i] 

        else :
            for j in range(start_a + 1 , start_a + 1 + t[i]) :
                a_list.append(j)

            start_a += t[i]

    elif d[i] == 'L' :
        if i == 0 :
            for j in range(0, -1 * (t[i] + 1), -1) :
                a_list.append(j)

            start_a = -1 * t[i]

        else :
            for j in range(start_a - 1, start_a - 1 -1*t[i] , -1) :
                a_list.append(j)

            start_a -= t[i]
    
for i in range(m) :
    if d2[i] == 'R' :
        if i == 0 :
            for j in range(start_b, t2[i] + 1) :
                b_list.append(j)

            start_b = t2[i] 

        else :
            for j in range(start_b + 1 , start_b + 1 + t2[i]) :
                b_list.append(j)

            start_b += t2[i]

    elif d2[i] == 'L' :
        if i == 0 :
            for j in range(0, -1 * (t2[i] + 1), -1) :
                b_list.append(j)

            start_b = -1 * t2[i]

        else :
            for j in range(start_b - 1, start_b - 1 -1*t2[i] , -1) :
                b_list.append(j)

            start_b -= t2[i]

solve = -1

for num in range(1, len(a_list)) :
    if a_list[num] == b_list[num] :
        solve = num
        break

print(solve)











    

        

        

            
