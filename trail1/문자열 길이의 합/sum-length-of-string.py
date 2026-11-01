n = int(input())
sum = 0
cnt = 0

for i in range(n) :
    r = input()
    sum += len(r)

    if r[0] == 'a' :
        cnt += 1

print(sum, cnt)
    

    