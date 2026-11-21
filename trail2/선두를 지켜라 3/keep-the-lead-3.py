N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

time = sum(t)

start_a = 1
start_b = 1

a_list = [0] * (time + 1)
b_list = [0] * (time + 1)

for i in range(N) :
    for j in range(start_a, start_a + t[i]) :
        a_list[j] = a_list[j-1] + v[i]

    start_a += t[i]

for i in range(M) :
    for j in range(start_b, start_b + t2[i]) :
        b_list[j] = b_list[j-1] + v2[i]

    start_b += t2[i]

solve_list = []

for k in range(time + 1) :
    if k == 0 :
        solve_list.append('z')

    elif a_list[k] > b_list[k] :
        solve_list.append('a')

    elif a_list[k] < b_list[k] :
        solve_list.append('b')

    elif a_list[k] == b_list[k] :
        solve_list.append('c')

cnt = 0

for elem in range(1, time + 1) :
    if solve_list[elem] != solve_list[elem-1] :
        cnt += 1

print(cnt)

