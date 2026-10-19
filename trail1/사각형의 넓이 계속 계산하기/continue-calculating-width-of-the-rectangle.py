while True :
    x, y, s = map(str, input().split())

    print(f"{int(x) * int(y)}")

    if s == "C" :
        break