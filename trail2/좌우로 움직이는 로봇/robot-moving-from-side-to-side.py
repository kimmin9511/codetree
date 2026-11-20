n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)


offset = 2000000

a_list = [0] * (offset+1)
b_list = [0] * (offset+1)

start_a = 1
start_b = 1

for i in range(n) :
    if d[i] == 'R' :
        for j in range(start_a, start_a + t[i]) :
            a_list[j] = a_list[j-1] + 1

        start_a = start_a + t[i]

    elif d[i] == 'L' :
        for j in range(start_a, start_a + t[i]) :
            a_list[j] = a_list[j-1] - 1

        start_a = start_a + t[i]

for i in range(m) :
    if d_b[i] == 'R' :
        for j in range(start_b, start_b + t_b[i]) :
            b_list[j] = b_list[j-1] + 1

        start_b = start_b + t_b[i]

    elif d_b[i] == 'L' :
        for j in range(start_b, start_b + t_b[i]) :
            b_list[j] = b_list[j-1] - 1

        start_b = start_b + t_b[i]

for k in range(1, offset+1) :
    if a_list[k] == 0 and a_list[k+1] == 0 :
        a_list = a_list[:k]
        break

for k in range(1, offset) :
    if b_list[k] == 0 and b_list[k+1] == 0 :
        b_list = b_list[:k]
        break

cnt = 0

if len(a_list) > len(b_list) :
    for num in range(1, len(b_list)) :
        if a_list[num] == b_list[num] :
            if a_list[num-1] != b_list[num-1] :
                cnt += 1

    for num in range(len(b_list) + 1, len(a_list)) :
        if a_list[num] == b_list[-1] :
            cnt += 1

elif len(a_list) < len(b_list) :
    for num in range(1, len(a_list)) :
        if a_list[num] == b_list[num] :
            if a_list[num-1] != b_list[num-1] :
                cnt += 1

    for num in range(len(a_list) + 1, len(b_list)) :
        if b_list[num] == a_list[-1] :
            cnt += 1

else :
    for num in range(1, len(a_list)) :
        if a_list[num] == b_list[num] :
            if a_list[num-1] != b_list[num-1] :
                cnt += 1

print(cnt)