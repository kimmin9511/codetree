count_arr = [0 for _ in range(6)] 

arr = list(map(int, input().split()))

for i in arr :
    count_arr[i-1] += 1

for i in range(1, 7) :
    print(f"{i} - {count_arr[i-1]}")