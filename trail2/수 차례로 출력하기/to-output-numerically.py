n = int(input())

def num_1(k) :
    if k == 0 :
        return

    num_1(k-1)
    print(k, end=" ")


def num_2(k) :
    if k == 0 :
        return

    print(k, end=" ")
    num_2(k-1)
    

num_1(n)
print()
num_2(n)