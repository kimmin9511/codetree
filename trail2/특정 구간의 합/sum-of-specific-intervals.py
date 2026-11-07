n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


def plus() :
    global arr

    for i in queries :
        sum = 0
        for j in range(i[0], i[1]+1) :
            sum += arr[j-1]
        print(sum)

plus()

    
