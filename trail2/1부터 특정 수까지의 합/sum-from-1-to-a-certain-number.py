def add(s) :
    sum = 0
    for i in range(1, s+1) :
        sum += i
    sum //= 10
    return sum


n = int(input())
total_num = add(n)
print(total_num)

