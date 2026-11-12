MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))


class lower :
    def __init__(self, a, b) :
        self.name = a
        self.name_score = b

    
min_point = 100
low_name = ''
for info in users :
    x, y = info
    i = lower(x, y)

    if i.name_score <= min_point :
        low_name = i.name
        min_point = i.name_score


print(f"{low_name} {min_point}")

    



    

