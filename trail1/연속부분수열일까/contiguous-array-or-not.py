a, b = map(int, input().split())

n_a = list(map(int, input().split()))

n_b = list(map(int, input().split()))

found = False


for i in range(a-b+1) :
    if n_a[i] == n_b[0] :
        cnt = 0
        for j in range(b) :
            if n_a[i+j] == n_b[j] :
                cnt += 1
                
            else :
                break

        if cnt == b :
            found = True
            break
    
if found : 
    print("Yes")

else :
    print("No")

        

    

    

    


        

