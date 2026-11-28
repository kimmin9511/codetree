# board = [list(map(int, input().split())) for _ in range(19)]

# def in_range(a, b) :
#     return 0 <= a < 19 and 0 <= b < 19

# solve = 0
# x, y = 0, 0

# for i in range(19) :
#     for j in range(19) :
#             if board[i][j] != 0 :
#                 cnt = 0

#                 for k in range(1, 5) :
#                     if not in_range(i+k, j) or board[i][j] != board[i+k][j] :
#                         cnt = 1

#                 if cnt == 1 :
#                     cnt = 0
                        

#                 else :
#                     x, y = i+2, j
#                     solve = board[i][j]


#                 for k in range(1, 5) :
#                     if not in_range(i, j+k) or board[i][j] != board[i][j+k] :
#                         cnt = 1

#                 if cnt == 1 :
#                     cnt = 0
                    

#                 else :
#                     x, y = i, j+2
#                     solve = board[i][j]
                        

#                 for k in range(1, 5) :
#                     if not in_range(i+k, j+k) or board[i][j] != board[i+k][j+k] :
#                         cnt = 1

#                 if cnt == 1 :
#                     cnt = 0

#                 else :
#                     x, y = i+2, j+2
#                     solve = board[i][j]

#                 for k in range(1, 5) : 
#                     if not in_range(i-k, j+k) or board[i][j] != board[i-k][j+k] :
#                         cnt = 1

#                 if cnt == 1 :
#                     cnt = 0
                        
#                 else :
#                     x, y = i-2, j+2
#                     solve = board[i][j]

# print(solve)
# if solve == 1 or solve == 2 :
#     print(x+1, y+1) 

board = [list(map(int, input().split())) for _ in range(19)]


dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def in_range(a,b) :
    return 0<=a<19 and 0<=b<19

def solve():
    for x in range(19):
        for y in range(19):
            
            if board[x][y] != 0:
                color = board[x][y]
                
                for i in range(4):
                    
                    cnt = 1
                    cx = x + dx[i]
                    cy = y + dy[i]
                    
                    while in_range(cx,cy) and board[cx][cy] == color:
                        cnt += 1
                        cx += dx[i]
                        cy += dy[i]
                    
                    
                    if cnt == 5:
                        print(color)
                        
                        mid_x = x + 2 * dx[i]
                        mid_y = y + 2 * dy[i]
                        print(mid_x + 1, mid_y + 1) 
                        return

    print(0)

solve()