n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

max_num = 1000000

a_list = [0] * (max_num+1)
b_list = [0] * (max_num+1)

start_a = 1
start_b = 1

for i in range(n) :
    for j in range(start_a, start_a + t[i]) :
        a_list[j] = a_list[j-1] + v[i]

    start_a += t[i]

for i in range(m) :
    for j in range(start_b, start_b + t2[i]) :
        b_list[j] = b_list[j-1] + v2[i]

    start_b += t2[i]


_list = []

for k in range(0, sum(t) + 1) :
    if a_list[k] > b_list[k] :
        _list.append('a')

    elif a_list[k] < b_list[k] :
        _list.append('b')



cnt = 0

solve_list = [w for w in _list if w != 0]

for k in range(len(solve_list) - 1) :
    if solve_list[k] != solve_list[k+1] :
        cnt += 1

print(cnt)