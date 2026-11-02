s, q = map(str, input().split())

for i in range(int(q)) :
    a, b, c = map(str, input().split())

    if int(a) == 1 :
        b, c = int(b), int(c)
        arr = list(s)
        k = arr[b-1]
        arr[b-1] = arr[c-1]
        arr[c-1] = k

        s = ''.join(arr)


    elif int(a) == 2 :
        for j in range(len(s)) :
            arr = list(s)
            if arr[j] == b :
                arr[j] = c

            s = ''.join(arr)

    print(s)

    