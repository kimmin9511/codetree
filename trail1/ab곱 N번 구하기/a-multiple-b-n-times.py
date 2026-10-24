n = int(input())

for i in range(n) :
    
    a, b = map(int, input().split())
    sum_val = 1

    for j in range(a, b+1) :
        sum_val *= j 

    print(sum_val)
