board = [list(map(int, input().split())) for _ in range(19)]

def in_range(a, b) :
    return 0 <= a < 19 and 0 <= b < 19

solve = 0
x, y = 0, 0

for i in range(19) :
    for j in range(19) :
            if board[i][j] != 0 :
                cnt = 0

                for k in range(1, 5) :
                    if not in_range(i+k, j) or board[i][j] != board[i+k][j] :
                        cnt = 1

                if cnt == 1 :
                    cnt = 0
                        

                else :
                    x, y = i+2, j
                    solve = board[i][j]


                for k in range(1, 5) :
                    if not in_range(i, j+k) or board[i][j] != board[i][j+k] :
                        cnt = 1

                if cnt == 1 :
                    cnt = 0
                    

                else :
                    x, y = i, j+2
                    solve = board[i][j]
                        

                for k in range(1, 5) :
                    if not in_range(i+k, j+k) or board[i][j] != board[i+k][j+k] :
                        cnt = 1

                if cnt == 1 :
                    cnt = 0

                else :
                    x, y = i+2, j+2
                    solve = board[i][j]

                for k in range(1, 5) : 
                    if not in_range(i-k, j+k) or board[i][j] != board[i-k][j+k] :
                        cnt = 1

                if cnt == 1 :
                    cnt = 0
                        
                else :
                    x, y = i-2, j+2
                    solve = board[i][j]

print(solve)
if solve == 1 or solve == 2 :
    print(x+1, y+1) 