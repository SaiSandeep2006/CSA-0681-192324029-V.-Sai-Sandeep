def game(board):
    def coun(board, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        liveneighbors = 0
        for dr, dc in directions:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(board) and 0 <= cc < len(board[0]) and abs(board[rr][cc]) == 1:
                liveneighbors += 1
        return liveneighbors
    rows, cols = len(board), len(board[0])
    nextstate = [[0] * cols for _ in range(rows)]    
    for r in range(rows):
        for c in range(cols):
            liveneighbors = coun(board, r, c)           
            if board[r][c] == 1:
                if liveneighbors < 2 or liveneighbors > 3:
                    nextstate[r][c] = 0  
                else:
                    nextstate[r][c] = 1  
            else:
                if liveneighbors == 3:
                    nextstate[r][c] = 1
                else:
                    nextstate[r][c] = 0 
    for r in range(rows):
        for c in range(cols):
            board[r][c] = nextstate[r][c]
board1 = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
game(board1)
print(board1)