n = int(input())
arr = list(map(int, input().split()))


def f(k) :
    if k == 0 :
        return arr[0]

    return max(f(k-1), arr[k])

print(f(n-1))