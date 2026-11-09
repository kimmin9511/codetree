n = int(input())
arr = list(map(int, input().split()))


def find_max(arr, n):
   
    if n == 1:
        return arr[0]

    
    max_value = find_max(arr, n - 1)

    
    if arr[n - 1] > max_value:
        return arr[n - 1]
    else:
        return max_value


print(find_max(arr, n))