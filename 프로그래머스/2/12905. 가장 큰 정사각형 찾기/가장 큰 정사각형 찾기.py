def solution(board):
    
    # 행과 열의 크기 구하기
    n = len(board)
    m = len(board[0])
    
    max_square = 0

    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0: # 첫 행 또는 첫 열
                dp[i][j] = board[i][j]
            elif board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
            max_square = max(max_square, dp[i][j])
    
    return max_square*max_square