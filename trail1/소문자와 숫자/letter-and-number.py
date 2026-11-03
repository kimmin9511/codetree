n = input()

for i in n :
    if i.isalpha() == True :
        print(i.lower(), end="")

    elif i.isdigit() == True :
        print(i, end="")