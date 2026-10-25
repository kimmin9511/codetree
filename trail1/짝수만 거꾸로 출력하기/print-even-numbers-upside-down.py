n = int(input())
arr = list(map(int, input().split()))
a = list()

for i in arr :
    if i % 2 == 0 :
        a.append(i)

for i in a[::-1] :
    print(i, end=" ")

        
