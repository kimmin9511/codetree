n = int(input())
nums = list(map(int, input().split()))

max_val = -1

for i in nums :
    if nums.count(i) == 1 :
        

        if max_val < i :
            max_val = i

print(max_val)

    
        