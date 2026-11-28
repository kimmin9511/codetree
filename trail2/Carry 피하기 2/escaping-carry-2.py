n = int(input())
arr = [int(input()) for _ in range(n)]

min_val = -1

sum = 0

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            sum = arr[i] % 10 + arr[j] % 10 + arr[k] % 10
            
            if sum < 10 :
                if arr[i] >= 10 or arr[j] >= 10 or arr[k] >= 10 :
                    sum = (arr[i] // 10) % 10 + (arr[j] // 10) % 10 + (arr[k] // 10) % 10
                    
                    if sum < 10 :
                        if arr[i] >= 100 or arr[j] >= 100 or arr[k] >= 100 :
                            sum = (arr[i] // 100)%10 + (arr[j] // 100)%10 + (arr[k] // 100) % 10
                            
                            if sum < 10 :
                                if arr[i] >= 1000 or arr[j] >= 1000 or arr[k] >= 1000 :
                                    sum = (arr[i] // 1000)%10 + (arr[j] // 1000)%10 + (arr[k] // 1000)%10
                                    
                                    if sum < 10 :
                                        if arr[i] >= 10000 or arr[j] >= 10000 or arr[k] >= 10000 :
                                            sum = arr[i] // 10000 + arr[j] // 10000 + arr[k] // 10000
                                            
                                            if sum < 10 :
                                                if arr[i] + arr[j] + arr[k] >= min_val :
                                                    min_val = arr[i] + arr[j] + arr[k]

                                        else :
                                            if arr[i] + arr[j] + arr[k] >= min_val :
                                                min_val = arr[i] + arr[j] + arr[k]

                                else :
                                    if arr[i] + arr[j] + arr[k] >= min_val :
                                        min_val = arr[i] + arr[j] + arr[k]

                        else :
                            if arr[i] + arr[j] + arr[k] >= min_val :
                                min_val = arr[i] + arr[j] + arr[k]

                else :
                    if arr[i] + arr[j] + arr[k] >= min_val :
                        min_val = arr[i] + arr[j] + arr[k]

print(min_val)