def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    while True:
        remove = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    remove.update([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])

        if not remove:
            break

        answer += len(remove)
        for a, b in remove:
            board[a][b] = ''
            
        for col in range(n):
            stack = [board[row][col] for row in range(m) if board[row][col] != '']
            # 빈 공간을 채우고 블록을 아래로 이동
            for row in range(m - len(stack)):
                board[row][col] = ''
            for row in range(m - len(stack), m):
                board[row][col] = stack[row - (m - len(stack))]
        
    return answer