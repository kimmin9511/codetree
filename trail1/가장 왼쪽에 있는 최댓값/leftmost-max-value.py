n = int(input())
arr = list(map(int, input().split()))

idx_number = []

while True :
    max_val = max(arr) 
    max_idx = arr.index(max_val)
    idx_number.append(max_idx+1)

    arr = arr[:max_idx]

    if max_idx == 0 :
        break

for i in idx_number :
    print(i, end=" ")



    



        



    
