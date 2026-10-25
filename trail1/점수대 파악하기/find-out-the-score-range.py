count_arr = [0 for _ in range(10)] 

arr = list(map(int, input().split()))

for i in arr :

    if i == 0 :
        break

    elif i >= 10 :
        i = i // 10
        count_arr[i-1] += 1

for i in range(100, 0, -10) :
    print(f"{i} - {count_arr[i//10 -1]}")