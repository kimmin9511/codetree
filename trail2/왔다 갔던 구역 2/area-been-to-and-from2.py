n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)


offset = 100
_list = [0] * (offset*n+1)
num = 0

for i in range(n) :
    if dir[i] == 'R' :
        for j in range(num + offset, num + x[i] + offset) :
            _list[j] += 1

        num += x[i]

    if dir[i] == 'L' :
        for j in range(num - x[i] + offset, num + offset) :
            _list[j] += 1

        num -= x[i]

cnt = 0
for k in _list :
    if k >= 2 :
        cnt +=1

print(cnt)
