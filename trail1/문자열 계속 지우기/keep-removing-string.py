A = input()
B = input()

len_a, len_b = len(A), len(B) 

list_a, list_b = list(A), list(B)

while True :
    idx = -1
    for i in range(len_a - len_b + 1) :
        if list_a[i] == list_b[0] :
            boolean = True
            for j in range(len_b) :
                if list_a[i+j] != list_b[j] :
                    boolean = False
                    break

            if boolean :
                idx = i
                break

    if idx == -1 :
        break

    list_a = list_a[:idx] + list_a[idx+len_b:]
    len_a = len(list_a)



print(''.join(list_a))