a, b, c = map(int, input().split())

def choice_num(n, m, k) :
    if n <= m and n <= k :
        return n
    elif m <= n and m <= k :
        return m

    elif k <= n and k <= m :
        return k


print(choice_num(a, b, c))
