str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

for i in queries :
    if i == 1 :
        str = str[1:] + str[0]
    
    elif i == 2 :
        str = str[-1] + str[:-1]

    elif i == 3 :
        arr=[]
        for j in range(1, len(str)+1) :
            arr.append(str[-1*j])

        str = ''.join(arr)


    print(str)


    



            



        
        
