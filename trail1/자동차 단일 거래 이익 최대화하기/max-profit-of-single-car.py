n = int(input())
price = list(map(int, input().split()))

max = 0

for i in range(n) :
    for j in range(n) :
        if i < j :
            if price[j] - price[i] > max :
                max = price[j] - price[i]
    

print(max)
