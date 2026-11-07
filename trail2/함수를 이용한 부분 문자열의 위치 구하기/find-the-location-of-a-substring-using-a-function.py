text = input()
pattern = input()

def modify(k) :
    if text[k] == pattern[0] :
        return True

    else :
        return False


for i in range(len(text) - len(pattern) +1) :
    cnt = 0
    idx = -1
    if modify(i) :
        for j in range(len(pattern)) :
            if text[i+j] == pattern[j] :
                cnt += 1

        if cnt == len(pattern) :
            idx = i
            break

print(idx)


        

    



    
