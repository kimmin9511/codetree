n = int(input())
nums = list(map(int, input().split()))


nums.sort() 
arr = []

for i in range(n) :
    arr.append(nums[i] + nums[2*n-i-1])

arr.sort()

print(arr[n-1])
    
