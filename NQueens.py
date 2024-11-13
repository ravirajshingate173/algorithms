def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
    
def is_safe(board,row,col,n):
    
    for i in range(row):
        if (board[i][col]=="Q"):
            return False
    
    i,j=row,col
    while(i>=0 and j>=0):
        if (board[i][j]=="Q"):
            return False
        
        i-=1
        j-=1
    
    i,j=row,col
    while(i>=0 and j<n):
        if (board[i][j]=="Q"):
            return False
        
        i-=1
        j+=1   
     
    return True

def solve_n_queens(board,row,n):
    
    if(row==n):
        print_board(board)
        return True
    
    for col in range(n):
        
        if(is_safe(board,row,col,n)):
            board[row][col]="Q"
            
            if(solve_n_queens(board,row+1,n)):
                return True
            board[row][col]="."
            
    return False
    
def n_queens_first_queen_placed(n,first_row=0,first_col=0):
    
    board=[["."for _ in range(n)] for _ in range(n)]
    
    board[first_row][first_col]="Q"
    
    if not (solve_n_queens(board,first_row+1,n)):
        print("No solutions found")
        
n_queens_first_queen_placed(4,0,3)
