for i in range(10) :
    x = input()

    if x == 'END' :
        break

    else :
        for j in range(-1, -1*len(x)-1, -1) :
            print(x[j], end="")

    print()