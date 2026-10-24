n = int(input())
val = 1

for i in range(n) :
    for j in range(i) :
        print(" ", end=" ")

    for j in range(n-i) :
        print(val, end=" ")

        val+=1

        if val > 9 :
            val = 1

    print()
