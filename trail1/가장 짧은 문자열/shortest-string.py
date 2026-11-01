a = input()
b = input()
c = input()

if len(a) >= len(b) and len(a) >= len(c) :
    if len(b) >= len(c) :
        print(len(a) - len(c))

    elif len(b) <= len(c) :
        print(len(a) - len(b))

elif len(b) >= len(a) and len(b) >= len(c) :
    if len(a) >= len(c) :
        print(len(b) - len(c))

    elif len(a) <= len(c) :
        print(len(b) - len(a))

elif len(c) >= len(a) and len(c) >= len(b) :
    if len(a) >= len(b) :
        print(len(c) - len(b))

    elif len(a) <= len(b) :
        print(len(c) - len(a))

