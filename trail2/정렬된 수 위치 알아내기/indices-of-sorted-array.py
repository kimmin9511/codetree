n = int(input())
sequence = list(map(int, input().split()))


class info :
    def __init__(self, a, b) :
        self.num = a
        self.idx = b


_list = []

for i in range(n) :
    _list.append(info(sequence[i], i+1))

_list.sort(key = lambda x : x.num)


num_to_rank = [0] * (n+1)

for rank, k in enumerate(_list, start = 1) :
    num_to_rank[k.idx] = rank


for j in num_to_rank[1:] :
    print(j, end=" ")
