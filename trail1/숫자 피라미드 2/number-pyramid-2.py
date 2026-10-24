n = int(input())

val = 1

for i in range(n) :
    for j in range(i+1) :
        print(val, end=" ")
        val +=1

    print()