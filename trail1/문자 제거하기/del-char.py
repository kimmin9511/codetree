n = input()

arr = list(n)

while True :
    num = int(input())
    if num >= len(arr) :
        arr.pop(-1)

    else :
        arr.pop(num)
    
    
    str = ''.join(arr)
    print(str)

    if len(str) == 1 :
        break



    