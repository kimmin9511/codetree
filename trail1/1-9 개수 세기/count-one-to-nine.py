n = int(input())

arr = list(map(int, input().split()))

count_arr = [0 for i in range(9)]

for i in arr :
    count_arr[i-1] += 1

for i in range(0,9) :
    print(count_arr[i])